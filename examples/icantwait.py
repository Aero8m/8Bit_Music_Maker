BPM = 129
SCALES = "f-"
DBTIME = 1
BS = 1
INFO = """
===============================
    8Bit Music Maker示例乐谱  
   d0tc0mmie 《I Can't Wait》 
      Powered By Aero8m
===============================     
"""
TRACK_SOUND = {"entry":"triangle","2st_track":"triangle","sax_solo":"triangle","drunk":"triangle",
               "sax_solo_drunk":'triangle',"bass1":"triangle","bass2":"triangle"}
TRACK_VOL = {"entry":0.6,"2st_track":0.5,"sax_solo":0.8,"drunk":0.5,"sax_solo_drunk":0.5,
             "bass1":0.4, "bass2":0.4}
TRACKS = {"entry":"""
call drunk
0.5 7+-1
0.5 1
0.5 5

call 2st_track
call bass1

1 6
1 5
1 6
1 2
1 3
1 5
1 6
1 5
1 6
1 2
1 3
1 5
1 6
1 5
1 6
1 2
1 3
1 5
1 1+1
1 7
1 5
1 2
1 3
1 5
1 6
1 5
1 6
1 2
1 3
1 5
1 6
1 5
1 6
1 5
1 6
1 2
1 3
1 5
1 6
1 5
1 6
1 2
1 3
1 5
1 6
1 5
1 6
1 2
1 3
1 5
1 1+1
1 7
1 5
1 2
1 3
1 5
1 6
1 5
1 6
1 2
1 3
1 5
1 6
2 5
wait_track sax_solo
1 6
1 5
1 6
1 2
1 3
1 5
1 6
1 5
1 6
1 2
1 3
1 5
1 6
1 5
1 6
1 2
1 3
1 5
1 1+1
1 7
1 5
1 2
1 3
1 5
1 6
1 5
1 6
1 2
1 3
1 5
1 6
1 5
1 6
1 5
1 6
1 2
1 3
1 5
1 6
1 5
1 6
1 2
1 3
1 5
1 6
1 5
1 6
1 2
1 3
1 5
1 1+1
1 7
1 5
1 2
1 3
1 5
1 6
1 5
1 6
1 2
1 3
1 5
1 6
2 5
""",
"2st_track":"""
0.25 3+1
1 3+1
1 7
1 1+1
1 3+1
0.25 2+1
1 2+1
1 7
1 1+1
1 5+1
0.5 3+1
2 0
2 6+1
2 0
2 5+1
0.5 3+1
1 1+1
2 1+1
4 7
4 1+1
1 7
2 7
4 6
4 7
1 5
2 5
4 5
4 6
1 5
1 7
1 1+1
1 5+1
0.25 3+1
1 3+1
1 7
1 1+1
1 3+1
0.25 2+1
1 2+1
1 7
1 1+1
1 5+1
0.5 3+1
2 0
2 6+1
2 0
2 5+1
0.5 3+1
0.5 1+1
0.25 2+1
1 2+1
1 7
1 1+1
1 5+1

call sax_solo
wait_track sax_solo

0.25 3+1
0.25 0
0.25 2+1
0.25 0
0.25 3+1
0.25 0
0.25 2+1
0.25 0

call bass2

0.25 3+1
1 3
1 7
1 1+1
1 3+1
0.25 2+1
1 2+1
1 7
1 1+1
1 5+1
0.5 3+1
2 0
2 6+1
2 0
2 5+1
0.5 3+1
0.5 1+1
0.25 2+1
1 2+1
1 7
1 1+1
1 5+1
0.25 3+1
1 3+1
1 7
1 1+1
1 3+1
0.25 2+1
1 2+1
1 7
1 1+1
1 5+1
0.5 3+1
2 0
2 6+1
2 0
2 5+1
0.5 3+1
0.5 1+1
0.25 2+1
""",
"sax_solo":"""
call sax_solo_drunk

2 0
2 6+-1
2 1
2 6+-1
2 3
4 3
4 5
2 0
1 2
2 1
2 1
2 6+-1
2 1
2 2
2 0
2 1

2 0
2 6+-1
2 1
2 6+-1
2 3
4 3
4 5
2 0
1 2
2 1
2 1
2 6+-1
2 1
2 2
2 0
2 1

2 0
2 6
4 6
4 3
2 0
2 3
4 3
4 2
2 0
1 2
2 1
1 3
0.5 3

2 0
2 6
4 6
4 3
2 0
2 3
4 3
4 2
2 0
1 2
2 1
2 1
0.5 1

1 e=noise
1 0
""",
"drunk":"""
0.5 e=kick
0.5 e=kick
0.5 e=kick


2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
4 e=snare
4 e=snare
4 e=hihat
4 e=snare


2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat


2 e=kick
2 e=hihat
4 e=snare
4 e=snare
4 e=hihat
4 e=snare


2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
4 e=snare
4 e=snare
4 e=hihat
4 e=snare


2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
4 e=snare
4 e=snare
4 e=hihat
4 e=snare


2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
4 e=snare
4 e=snare
4 e=hihat
4 e=snare


2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
4 e=snare
4 e=snare
4 e=hihat
4 e=snare


2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
4 e=snare
4 e=snare
4 e=hihat
4 e=snare

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
4 e=snare
4 e=snare
4 e=hihat
4 e=snare

wait_track sax_solo

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
4 e=snare
4 e=snare
4 e=hihat
4 e=snare

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
4 e=snare
4 e=snare
4 e=hihat
4 e=snare

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
4 e=snare
4 e=snare
4 e=hihat
4 e=snare


2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
4 e=snare
4 e=snare
4 e=hihat
4 e=snare

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
4 e=snare
4 e=snare
4 e=hihat
4 e=snare

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
4 e=snare
4 e=snare
4 e=hihat
4 e=snare

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
4 e=snare
4 e=snare
4 e=hihat
4 e=snare

1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
4 e=snare
4 e=snare
4 e=hihat
4 e=snare
""",
"sax_solo_drunk":"""
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick

1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick
1 e=kick

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat


2 e=kick
2 e=hihat
2 e=snare
2 e=hihat

2 e=kick
2 e=hihat
2 e=snare
2 e=hihat


2 e=kick
2 e=hihat
2 e=snare
2 e=hihat
4 e=snare
4 e=snare
4 e=hihat
4 e=snare
"""
,"bass1":"""
2 3
4 0
4 3
2 0
4 3
2 0
4 0
4 3
2 0
4 3
2 0

2 3
4 0
4 3
2 0
4 3
2 0
4 0
4 3
2 0
4 3
2 0

2 2
4 0
4 2
2 0
4 2
2 0
4 0
4 2
2 0
4 2
2 0

2 2
4 0
4 2
2 0
4 2
2 0
4 0
4 2
2 0
4 2
2 0

2 3
4 0
4 3
2 0
4 3
2 0
4 0
4 3
2 0
4 3
2 0

2 3
4 0
4 3
2 0
4 3
2 0
4 0
4 3
2 0
4 3
2 0

2 2
4 0
4 2
2 0
4 2
2 0
4 0
4 2
2 0
4 2
2 0

2 2
4 0
4 2
2 0
4 2
2 0
4 0
4 2
2 0
4 2
2 0

2 3
4 0
4 3
2 0
4 3
2 0
4 0
4 3
2 0
4 3
2 0

2 3
4 0
4 3
2 0
4 3
2 0
4 0
4 3
2 0
4 3
2 0

2 2
4 0
4 2
2 0
4 2
2 0
4 0
4 2
2 0
4 2
2 0

2 2
4 0
4 2
2 0
4 2
2 0
4 0
4 2
2 0
4 2
2 0

2 3
4 0
4 3
2 0
4 3
2 0
4 0
4 3
2 0
4 3
2 0

2 3
4 0
4 3
2 0
4 3
2 0
4 0
4 3
2 0
4 3
2 0

2 2
4 0
4 2
2 0
4 2
2 0
4 0
4 2
2 0
4 2
2 0

2 2
4 0
4 2
2 0
4 2
2 0
4 0
4 2
2 0
4 2
2 0
""",
"bass2":"""
2 3
4 0
4 3
2 0
4 3
2 0
4 0
4 3
2 0
4 3
2 0

2 3
4 0
4 3
2 0
4 3
2 0
4 0
4 3
2 0
4 3
2 0

2 2
4 0
4 2
2 0
4 2
2 0
4 0
4 2
2 0
4 2
2 0

2 2
4 0
4 2
2 0
4 2
2 0
4 0
4 2
2 0
4 2
2 0

2 3
4 0
4 3
2 0
4 3
2 0
4 0
4 3
2 0
4 3
2 0

2 3
4 0
4 3
2 0
4 3
2 0
4 0
4 3
2 0
4 3
2 0

2 2
4 0
4 2
2 0
4 2
2 0
4 0
4 2
2 0
4 2
2 0

2 2
4 0
4 2
2 0
4 2
2 0
4 0
4 2
2 0
4 2
2 0

2 3
4 0
4 3
2 0
4 3
2 0
4 0
4 3
2 0
4 3
2 0

2 3
4 0
4 3
2 0
4 3
2 0
4 0
4 3
2 0
4 3
2 0

2 2
4 0
4 2
2 0
4 2
2 0
4 0
4 2
2 0
4 2
2 0

2 2
4 0
4 2
2 0
4 2
2 0
4 0
4 2
2 0
4 2
2 0

2 3
4 0
4 3
2 0
4 3
2 0
4 0
4 3
2 0
4 3
2 0

2 3
4 0
4 3
2 0
4 3
2 0
4 0
4 3
2 0
4 3
2 0

2 2
4 0
4 2
2 0
4 2
2 0
4 0
4 2
2 0
4 2
2 0

2 2
4 0
4 2
2 0
4 2
2 0
4 0
4 2
2 0
4 2
2 0
"""}
