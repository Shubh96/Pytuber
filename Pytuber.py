# ==================================import statements====================================

from pytube import YouTube
from pytube.exceptions import RegexMatchError
import requests
from bs4 import BeautifulSoup
import win32com.client as wincl
from tkinter import *
from tkinter import filedialog
import re

# ========================initializing the speaker voice and validation regex===========================
speaker = wincl.Dispatch("SAPI.SpVoice")

# ==================================function definition to download video==============================


def video_download(download_url):
    try:
        yt_object = YouTube(download_url)
        dl_video_stream = yt_object.streams.first()

        speaker.Speak("Downloading Video")
        dl_video_stream.download(download_location)
    except RegexMatchError:
        take_input()


def take_input():
    speaker.Speak("Invalid URL! Please enter a YouTube video link")
    video_link = input('Enter the video link: ')
    video_download(video_link)
# ===========================function definition to generate playlist by web scraping==========================


def playlist_generate():
    html_doc = requests.get(playlist_link_input).text
    parsed_doc = BeautifulSoup(html_doc, 'html.parser')
    playlist_anchor = parsed_doc('a', {'class': 'pl-video-title-link'})

    if len(playlist_anchor) == 0:
        playlist_anchor = parsed_doc('a', {'class': 'playlist-video'})

    return playlist_anchor

# ===========================function definition to create playlist by web scraping==========================


def create_playlist():
    playlist = []

    for pla in pl_anchor:
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


# ========================================global statements========================================

speaker.Speak("Press 1 to download a playlist")
print("1. Download a playlist")

speaker.Speak("Press 2 to download single video")
print("2. Download single video")

speaker.Speak("Press any other key to exit")
print("Press any other key to exit")

userMenuChoice = int(input("Enter your choice: "))

if userMenuChoice == 1:

    speaker.Speak("Select download location")
    download_location = filedialog.askdirectory()

    speaker.Speak("Enter the playlist link")
    playlist_link_input = input('Enter the playlist link: ')

    pl_anchor = playlist_generate()

    while len(pl_anchor) == 0:
        speaker.Speak("Invalid URL! Please enter a YouTube playlist")
        playlist_link_input = input('Enter the playlist link: ')
        pl_anchor = playlist_generate()
    else:
        create_playlist()

elif userMenuChoice == 2:

    speaker.Speak("Select download location")
    download_location = filedialog.askdirectory()

    speaker.Speak("Enter the video link")
    video_link_input = input('Enter the video link: ')

    video_download(video_link_input)

    speaker.Speak("Video downloaded")
else:
    speaker.Speak("Thanks for using Pytuber.")
    sys.exit(0)