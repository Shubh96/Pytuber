from pytube import YouTube
import requests
from bs4 import BeautifulSoup
import win32com.client as wincl
from tkinter import *
from tkinter import filedialog

speaker = wincl.Dispatch("SAPI.SpVoice")


def video_download(video_link_input):
    yt_object = YouTube(video_link_input)
    dl_video_stream = yt_object.streams.first()
    dl_video_stream.download(download_location)


def playlist_generate():
    html_doc = requests.get(playlist_link_input).text
    parsed_doc = BeautifulSoup(html_doc, 'html.parser')
    playlist_anchor = parsed_doc('a', {'class': 'pl-video-title-link'})

    playlist = []

    for pla in playlist_anchor:
        playlist.append('https://www.youtube.com' + pla.get('href'))

    length = len(playlist)

    for i, pl in enumerate(playlist):
        speech = "Downloading video " + str(i + 1)
        speaker.Speak(speech)

        video_download(pl)

        if i < length:
            speech = "Video " + str(i + 1) + "downloaded."
            speaker.Speak(speech)
        else:
            speaker.Speak("Completed downloading playlist")


speaker.Speak("Press 1 to download a playlist")
print("1. Download a playlist")

speaker.Speak("Press 2 to download single video")
print("2. Download single video")

speaker.Speak("Press any other key to exit")
print("Press any other key to exit")

userMenuChoice = int(input("Enter your choice: "))

if userMenuChoice == 1:

    speaker.Speak("Enter the playlist link")
    playlist_link_input = input('Enter the playlist link: ')

    speaker.Speak("Select download location")
    download_location = filedialog.askdirectory()

    playlist_generate()

elif userMenuChoice == 2:

    speaker.Speak("Enter the video link")
    playlist_link_input = input('Enter the video link: ')

    speaker.Speak("Select download location")
    download_location = filedialog.askdirectory()

    speaker.Speak("Downloading Video")
    video_download(playlist_link_input)

    speaker.Speak("Video downloaded")
else:
    speaker.Speak("Thanks for using Pytuber.")
    sys.exit(0)
