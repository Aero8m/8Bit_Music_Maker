import time
import pygame
import numpy as np
from threading import Thread
import runpy
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=1024) 
# buffer=512 是关键：越小延迟越低，但太小会有爆音。512 或 1024 是平衡点。

def make_stereo(freq, duration_ms, wave_type="triangle", volume=0.8, bit_depth=8, sample_rate=44100):
    """
    生成 8-bit 风格音频或 EDM 鼓组
    参数:
        freq: 频率 (Hz) [鼓音忽略此参数]
        duration_ms: 持续时间 (毫秒)
        wave_type: 'square', 'triangle', 'noise' | 'kick', 'snare', 'hihat'
        volume: 音量 (0.0 ~ 1.0) -> 现已修复，在量化前应用
        bit_depth: 位深 (8 复古，16 清晰)
        sample_rate: 采样率
    """
    # 1. 严格类型防护
    freq = float(freq)
    duration_ms = float(duration_ms)
    volume = float(np.clip(volume, 0.0, 1.0))  # 确保音量在合法范围
    sample_rate = float(sample_rate)
    bit_depth = int(bit_depth)
    wave_type = wave_type.lower()

    n_samples = max(int(sample_rate * duration_ms / 1000), 2)
    t_sec = np.linspace(0, duration_ms / 1000, n_samples, endpoint=False)
    wave = np.zeros(n_samples, dtype=np.float64)

    # ================= 鼓组合成模块 =================
    if wave_type == 'kick':
        # EDM 底鼓: 指数下扫频 + 瞬态冲击
        freq_inst = 300 * np.exp(-t_sec * 12)
        phase = 2 * np.pi * np.cumsum(freq_inst) / sample_rate
        env = np.exp(-t_sec * 8)
        wave = np.sin(phase) * env
        click_len = min(int(sample_rate * 0.003), n_samples)
        if click_len > 0:
            wave[:click_len] *= np.linspace(1.6, 1.0, click_len)
        #wave *= 2
    elif wave_type == 'snare':
        # EDM 军鼓: 低频体感 + 高频响弦
        tone_freq = 210 * np.exp(-t_sec * 18)
        phase = 2 * np.pi * np.cumsum(tone_freq) / sample_rate
        tone = np.sin(phase)
        noise = np.random.randn(n_samples)
        noise[1:] -= 0.75 * noise[:-1]  # 高通模拟响弦
        env_tone = np.exp(-t_sec * 10)
        env_noise = np.exp(-t_sec * 22)
        wave = (tone * 0.55 + noise * 0.45) * (env_tone + env_noise)

    elif wave_type == 'hihat':
        # EDM 闭镲: 极短高频噪声 + 金属振荡
        noise = np.random.randn(n_samples)
        noise[1:] -= 0.92 * noise[:-1]  # 强高通
        metal = np.sign(np.sin(2 * np.pi * 8500 * t_sec)) * np.exp(-t_sec * 55)
        env = np.exp(-t_sec * 40)
        wave = (noise * 0.65 + metal * 0.35) * env

    # ================= 基础波形模块 =================
    elif wave_type == 'square':
        wave = np.sign(np.sin(2 * np.pi * freq * t_sec))
    elif wave_type == 'triangle':
        wave = 2 * np.abs(2 * (t_sec * freq - np.floor(0.5 + t_sec * freq))) - 1
    elif wave_type == 'noise':
        wave = np.random.uniform(-1, 1, n_samples) * 0.5
    else:
        raise ValueError(f"不支持的 wave_type: '{wave_type}'。可选: square, triangle, noise, kick, snare, hihat")

    # ==========================================
    # 【关键修复】音量调节移至位深压缩之前
    # ==========================================
    wave *= volume
    
    # 安全限幅 (防止音量过大导致后续裁剪失真)
    wave = np.clip(wave, -1.0, 1.0)

    # 3. 位深压缩 (Bit Crush)
    # 此时 wave 已经过音量衰减，量化效果会更自然
    if bit_depth < 16:
        levels = 2 ** bit_depth
        # 量化公式: round(x * steps) / steps
        wave = np.round(wave * (levels / 2.0)) / (levels / 2.0)

    # 4. 包络塑形 (鼓组保留瞬态，仅切极短尾部防爆音)
    if wave_type in ('kick', 'snare', 'hihat'):
        fade_out = min(int(sample_rate * 0.005), n_samples // 2)
        if fade_out > 0:
            wave[-fade_out:] *= np.linspace(1.0, 0.0, fade_out)
    else:
        # 基础波形使用标准淡入淡出
        fade_samples = int(sample_rate * 0.01)
        if n_samples > fade_samples * 2:
            wave[:fade_samples] *= np.linspace(0.0, 1.0, fade_samples)
            wave[-fade_samples:] *= np.linspace(1.0, 0.0, fade_samples)

    # 5. 转为立体声
    audio_stereo = np.column_stack((wave, wave))

    # 6. 最终防削波 & 转 16-bit PCM
    audio_stereo = np.clip(audio_stereo, -1.0, 1.0)
    return (audio_stereo * 32767).astype(np.int16)
    
def play_stereo(audio_stereo):
    if isinstance(audio_stereo,float) or isinstance(audio_stereo,int):
        time.sleep(audio_stereo)
        return
    sound = pygame.sndarray.make_sound(audio_stereo)
    sound.play()

base_scales_frequency = {
    # === 降F调（特别要求）===
    "f-":  [330, 370, 415, 440, 494, 554, 622, 659],
    "fm-": [330, 370, 392, 440, 494, 523, 587, 659],
    
    # === C 系列 ===
    "c":   [262, 294, 330, 349, 392, 440, 494, 523],
    "cm":  [262, 294, 311, 349, 392, 415, 466, 523],
    "c+":  [277, 311, 349, 370, 415, 466, 523, 554],
    "c+m": [277, 311, 330, 370, 415, 440, 494, 554],
    
    # === D 系列 ===
    "d":   [294, 330, 370, 392, 440, 494, 554, 587],
    "dm":  [294, 330, 349, 392, 440, 466, 523, 587],
    "d+":  [311, 349, 392, 415, 466, 523, 587, 622],
    "d+m": [311, 349, 370, 415, 466, 494, 554, 622],
    "d-":  [277, 311, 349, 370, 415, 466, 523, 554],
    "d-m": [277, 311, 330, 370, 415, 440, 494, 554],
    
    # === E 系列 ===
    "e":   [330, 370, 415, 440, 494, 554, 622, 659],
    "em":  [330, 370, 392, 440, 494, 523, 587, 659],
    "e-":  [311, 349, 392, 415, 466, 523, 587, 622],
    "e-m": [311, 349, 370, 415, 466, 494, 554, 622],
    
    # === F 系列 ===
    "f":   [349, 392, 440, 466, 523, 587, 659, 698],
    "fm":  [349, 392, 415, 466, 523, 554, 622, 698],
    "f+":  [370, 415, 466, 494, 554, 622, 698, 740],
    "f+m": [370, 415, 440, 494, 554, 587, 659, 740],
    
    # === G 系列 ===
    "g":   [392, 440, 494, 523, 587, 659, 740, 784],
    "gm":  [392, 440, 466, 523, 587, 622, 698, 784],
    "g+":  [415, 466, 523, 554, 622, 698, 784, 831],
    "g+m": [415, 466, 494, 554, 622, 659, 740, 831],
    "g-":  [370, 415, 466, 494, 554, 622, 698, 740],
    "g-m": [370, 415, 440, 494, 554, 587, 659, 740],
    
    # === A 系列 ===
    "a":   [440, 494, 554, 587, 659, 740, 831, 880],
    "am":  [440, 494, 523, 587, 659, 698, 784, 880],
    "a+":  [466, 523, 587, 622, 698, 784, 880, 932],
    "a+m": [466, 523, 554, 622, 698, 740, 831, 932],
    "a-":  [415, 466, 523, 554, 622, 698, 784, 831],
    "a-m": [415, 466, 494, 554, 622, 659, 740, 831],
    
    # === B 系列 ===
    "b":   [494, 554, 622, 659, 740, 831, 932, 988],
    "bm":  [494, 554, 587, 659, 740, 784, 880, 988],
    "b-":  [466, 523, 587, 622, 698, 784, 880, 932],
    "b-m": [466, 523, 554, 622, 698, 740, 831, 932],
}

def process_track(track,track_sound,track_vol):
    global bpm,scale,scale_base_list,dbtime,bs
    music_data_strings = track.split("\n")
    music_data = []
    for data_str in music_data_strings:
        if data_str == "":
            continue
        if data_str.split(" ")[0] == "sleep":
            tm = int(data_str.split(" ")[1])
            music_data.append((tm*dbtime/1000,0))
            continue
        if data_str.split(" ")[1] == "0":
            tp = float(data_str.split(" ")[0])
            tm = int(60/bpm*1000*(1/(tp))*dbtime)
            music_data.append((tm*dbtime/1000,0))
            continue
        if data_str.split(" ")[0] == "call":
            music_data.append((data_str,0))
            continue
        if data_str.split(" ")[0] == "goto":
            music_data.append((data_str,0))
            continue
        if data_str.split(" ")[0] == "wait_track":
            music_data.append((data_str,0))
            continue
        if "e=" in data_str.split(" ")[1]:
            tp = float(data_str.split(" ")[0])
            
            music_data.append((make_stereo(1,int(60/bpm*1000*(1/(tp))*dbtime),wave_type=data_str.split(" ")[1].replace("e=",""),volume=track_vol),int(60/bpm*1000*(1/(tp))*dbtime)))
            continue
        if data_str.split(" ")[0] == "play_audio":
            music_data.append((data_str,0))
            continue
        tp = float(data_str.split(" ")[0])
        sound = int(data_str.split(" ")[1].split("+")[0])
        bsound = 1
        if len(data_str.split("+")) == 2:
            if int(data_str.split(" ")[1].split("+")[1]) < 0:
                bsound /= abs(int(data_str.split(" ")[1].split("+")[1]))+1
            else:
                bsound += int(data_str.split(" ")[1].split("+")[1])
        
        music_data.append((make_stereo(base_scales_frequency[scale][sound-1]*bsound*bs,int(60/bpm*1000*(1/(tp))*dbtime),wave_type=track_sound,volume=track_vol),int(60/bpm*1000*(1/(tp))*dbtime)))
    return music_data

def track_thread_target(track_name, track_data):
    global tracks_start_flag
    while not tracks_start_flag[track_name]:
        time.sleep(0.0001)
    for i in range(len(track_data)):
        if isinstance(track_data[i][0],str):
            if track_data[i][0].split(" ")[0] == "call":
                print(f"轨道 {track_name} 异步唤起轨道 {track_data[i][0].split(" ")[1]}")
                tracks_start_flag[track_data[i][0].split(" ")[1]] = True
            elif track_data[i][0].split(" ")[0] == "goto":
                print(f"轨道 {track_name} 跳转到轨道 {track_data[i][0].split(" ")[1]}")
                tracks_start_flag[track_data[i][0].split(" ")[1]] = True
                while tracks_start_flag[track_data[i][0].split(" ")[1]]:
                    time.sleep(0.0001)
            elif track_data[i][0].split(" ")[0] == "wait_track":
                print(f"轨道 {track_name} 等待轨道 {track_data[i][0].split(" ")[1]}")
                while not tracks_start_flag[track_data[i][0].split(" ")[1]]:
                    time.sleep(0.0001)
                while tracks_start_flag[track_data[i][0].split(" ")[1]]:
                    time.sleep(0.0001)
            elif track_data[i][0].split(" ")[0] == "play_audio":
                audio_file = track_data[i][0].split(" ")[1]
                audio_vol = float(track_data[i][0].split(" ")[2])
                print(f"轨道 {track_name} 播放音频 {audio_file}")
                audio_mixer = pygame.mixer.Sound(audio_file)
                audio_mixer.set_volume(audio_vol)
                audio_mixer.play()
            continue
            
        print(f"轨道 {track_name} 正在播放第{i+1}个...")
        play_stereo(track_data[i][0])
        time.sleep(track_data[i][1]/1000)
    tracks_start_flag[track_name] = False
    print(f"轨道 {track_name} 播放完成!")

print("-"*30)
print("8Bit Music Maker By Aero8m")
print("Github 链接: https://github.com/Aero8m/8Bit_Music_Maker")
print("-"*30)
fileUrl = input("输入文件: ")
musicData = runpy.run_path(fileUrl)
bpm = musicData.get("BPM")
scale = musicData.get("SCALES").lower()
scale_base_list = base_scales_frequency[scale]
dbtime = float(musicData.get("DBTIME"))
bs = musicData.get("BS")
txt_tracks = musicData.get("TRACKS")
track_sound = musicData.get("TRACK_SOUND")
track_volume = musicData.get("TRACK_VOL")
tracks = {}
track_threads = []
tracks_start_flag = {}
start_flag = False
print(musicData.get("TRACK_VOL"))
if "entry" not in txt_tracks.keys():
    print("未找到entry轨道！请设置entry轨道！")
    exit()
print("正在处理音乐数据......")
for track_name in txt_tracks.keys():
    print(f"处理轨道 {track_name} 中...")
    tracks[track_name] = process_track(txt_tracks[track_name],track_sound[track_name],track_volume[track_name])
    tracks_start_flag[track_name] = False
    print(f"处理成功，找到{len(tracks[track_name])}个音符！")
print("全部轨道处理完成！")
print("正在创建轨道线程...")
for track_name in tracks:
    track_threads.append(Thread(target=track_thread_target, daemon=True, 
                                args=(track_name, tracks[track_name])))
    track_threads[-1].start()
    print(f"成功创建轨道{track_name}线程！")
input("按enter开始播放")
tracks_start_flag["entry"] = True
for track_thread in track_threads:
    track_thread.join()
print("播放完毕！")