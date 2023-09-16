from pytube import YouTube
import demucs.separate
import shutil
import os
import pathlib
import sys

url  = sys.argv[1]

try:
   video = YouTube(url)
   filename = f"{video.title}.mp4"
   stream = video.streams.filter(only_audio=True).first()
   stream.download(f'full/temp_{filename}')
   print("The video is downloaded in MP4")

except KeyError:
   print("Unable to fetch video information. Please check the video URL or your network connection.")

#remove 
source = f"FULL/temp_{filename}/{filename}" # Source path
destination = f"full/" #Destination path
dest = shutil.copy(source, destination) # Move the content of source to destination 

shutil.rmtree(f'FULL/temp_{filename}') #delete temp folder

#split drums from track
demucs.separate.main(["--mp3", "--two-stems", "drums", "-n", "mdx_extra", f"full/{filename}"])



