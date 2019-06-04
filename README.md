# dubpy

A python script to dub one youtube's audio over another youtube's video. This script will be augmented with some timing offset specifications and then integrated into a web service that allows users to select and dub videos in a browser.

## INSTALLATION:
```
$ python -m pip install --ignore-installed moviepy
$ python -m pip install youtube-dl
$ sudo add-apt-repository ppa:mc3man/trusty-media
$ sudo apt-get update
$ sudo apt-get install ffmpeg
$ ffmpeg -version
```

## USAGE EXAMPLES:
```
$ ffmpeg -i video.mkv -i audio.webm -c copy -map 0:v -map 1:a output.mkv
$ python3 dubpy.py youtubeVideoID youtubeAudioID
$ python3 dubpy.py HQUjviIH9PU 0_3CU_CkB-o
```
