# ==================================import statements====================================

from pytube import YouTube
import requests
from bs4 import BeautifulSoup
import win32com.client as wincl
from tkinter import *
from tkinter import filedialog
import re

# ========================initializing the speaker voice and validation regex===========================
speaker = wincl.Dispatch("SAPI.SpVoice")
ytvideo_regex = '^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$'


# ==================================function definition to download video==============================

def video_download(download_url):
    yt_object = YouTube(download_url)
    dl_video_stream = yt_object.streams.first()
    dl_video_stream.download(download_location)


# ==================================function definition to validate video==============================

def validate_video_url(video_link):
    matched = re.search(ytvideo_regex, video_link)

    if matched is None:
        speaker.Speak("Invalid URL! Please enter a YouTube video URL")
        video_link = input('Enter the video link: ')
        return validate_video_url(video_link)
    else:
        return video_link


# ===========================function definition to generate playlist by web scraping==========================

def playlist_generate():
    html_doc = requests.get(playlist_link_input).text
    parsed_doc = BeautifulSoup(html_doc, 'html.parser')
    playlist_anchor = parsed_doc('a', {'class': 'pl-video-title-link'})

    if len(playlist_anchor) == 0:
        playlist_anchor = parsed_doc('a', {'class': 'playlist-video'})

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


# ========================================global statements========================================

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
    video_link_input = input('Enter the video link: ')
    video_link_input = validate_video_url(video_link_input)

    speaker.Speak("Select download location")
    download_location = filedialog.askdirectory()

    speaker.Speak("Downloading Video")
    video_download(video_link_input)

    speaker.Speak("Video downloaded")
else:
    speaker.Speak("Thanks for using Pytuber.")
    sys.exit(0)