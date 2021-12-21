from pytube import YouTube as youtube
import time

def thumbnail(vid):
    return vid.thumbnail_url

def video(vid, location):
    vid.download(location)

def audio(vid, location):
    vid.download(location)

url = input("Input the URL of the video you want to download: ")

yt = youtube(url)

typee = input("Do you want the thumbnail, audio or video? (t/a/v): ")

if typee.lower() == "t":
    thumbnail = thumbnail(yt)
    print(thumbnail)
    time.sleep(10)
elif typee.lower() == "a":
    location = input("Inout the location where you want to download it: ")
    stream = yt.streams.get_audio_only()
    audio(stream, location)
    print("Downloaded")
    time.sleep(10)
elif typee.lower() == "v":
    location = input("Input the location where you want to download it: ")
    stream = yt.streams.get_highest_resolution()
    video(stream, location)
    print("Downloaded")
    time.sleep(10)
