"""
INSTALLATION:
--------------------------------------------------------------------------------
$ python -m pip install --ignore-installed moviepy

$ python -m pip install youtube-dl

$ sudo add-apt-repository ppa:mc3man/trusty-media
$ sudo apt-get update
$ sudo apt-get install ffmpeg
$ ffmpeg -version

USAGE EXAMPLES:
--------------------------------------------------------------------------------
$ ffmpeg -i video.mkv -i audio.webm -c copy -map 0:v -map 1:a output.mkv

$ python3 dubpy.py youtubeVideoID youtubeAudioID
$ python3 dubpy.py HQUjviIH9PU 0_3CU_CkB-o

"""
		
import sys
from youtube_dl import YoutubeDL

vVideoURL = "https://www.youtube.com/watch?v="+sys.argv[1];
aVideoURL = "https://www.youtube.com/watch?v="+sys.argv[2];

YoutubeDL({"outtmpl":"output/_v_.%(ext)s"}).download([vVideoURL])
YoutubeDL({"outtmpl":"output/_a_.%(ext)s"}).download([aVideoURL])

aFile = False;
vFile = False;

import os
import subprocess
files = os.listdir("./output");
for f in files:
	parts = f.split(".")
	if (parts[0]=="_a_"):
		aFile = "./output/" + f;
	if (parts[0]=="_v_"):
		vFile = "./output/" + f;

subprocess.call(['ffmpeg', '-i', vFile, '-i', aFile, '-c', 'copy','-map', '0:v', '-map', '1:a', 'output/output.mkv']);

for f in files:
	os.remove("./output/" + f)

