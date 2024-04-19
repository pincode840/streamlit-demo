from pytube import YouTube 
import os

yt = YouTube('https://youtu.be/Vy1JwiXHwI4?si=eZ1dsNDgphBMR0TR')
print(yt.title)
yt = yt.streams.get_highest_resolution().download()

filePath = yt.replace('mp4', 'mp3')
os.rename(yt, filePath)
print(f'name = {filePath}')