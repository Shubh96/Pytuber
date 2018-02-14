# ==================================import statements====================================
from pytube import YouTube
from pytube.exceptions import RegexMatchError
import requests
from requests.exceptions import *
from bs4 import BeautifulSoup
import win32com.client as wincl
from tkinter import *
from tkinter import filedialog
import os
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
        take_video_link_input()

#  ==================================function definition to take correct video link input==============================
def take_video_link_input():
    speaker.Speak("Invalid URL! Please enter a YouTube video link")
    video_link = input('Enter the video link: ')
    video_download(video_link)

#  ==================================function definition to take correct playlist link input==============================
def take_playlist_link_input():
    speaker.Speak("Please enter a proper YouTube playlist")
    global playlist_link_input
    playlist_link_input = input('Enter playlist link: ')
    playlist_generate(playlist_link_input)

# ===========================function definition to generate video links by web scraping==========================
def playlist_generate(pl_link):
    try:
        html_doc = requests.get(pl_link).text
        parsed_doc = BeautifulSoup(html_doc, 'html.parser')
        playlist_anchor = parsed_doc('a', {'class': 'pl-video-title-link'})

        if len(playlist_anchor) == 0:
            playlist_anchor = parsed_doc('a', {'class': 'playlist-video'})

        while len(playlist_anchor) == 0:
            take_playlist_link_input()
        else:
            create_playlist(playlist_anchor)

        return
    except (HTTPError,  ProxyError, MissingSchema, InvalidURL, ConnectionError, Timeout, URLRequired, TooManyRedirects, InvalidSchema):
        take_playlist_link_input()

# ======================================function definition to create playlist=====================================
def create_playlist(pl_anchor):
    playlist = []

    for pla in pl_anchor:
        playlist.append('https://www.youtube.com' + pla.get('href'))

    length = len(playlist)

    for i, pl in enumerate(playlist):
        speech = "Downloading video " + str(i + 1)
        speaker.Speak(speech)

        video_download(pl)

        if (i+1) < length:
            speech = "Video " + str(i + 1) + "downloaded."
            speaker.Speak(speech)
        else:
            speaker.Speak("Completed downloading playlist")

    return

#========================================================exit function=========================================
def quit():
    speaker.Speak("Thanks for using Pytuber.")
    sys.exit(0)

# ========================================global statements========================================
use_again = 'y'

while use_again == 'Y' or use_again == 'y':
    os.system('cls')
    speaker.Speak("Press 1 to download a playlist")
    print("1. Download a playlist")

    speaker.Speak("Press 2 to download single video")
    print("2. Download single video")

    speaker.Speak("Press any other key to exit")
    print("Press any other key to exit")

    userMenuChoice = input("Enter your choice: ")

    while not userMenuChoice.isdigit():
        speaker.Speak("Invalid choice. Please, enter a digit")
        userMenuChoice = input("Enter your choice: ")

    if int(userMenuChoice) == 1:

        speaker.Speak("Select download location")
        download_location = filedialog.askdirectory()

        speaker.Speak("Enter the playlist link")
        playlist_link_input = input('Enter the playlist link: ')

        playlist_generate(playlist_link_input)

    elif int(userMenuChoice) == 2:

        speaker.Speak("Select download location")
        download_location = filedialog.askdirectory()

        speaker.Speak("Enter the video link")
        video_link_input = input('Enter the video link: ')

        video_download(video_link_input)

        speaker.Speak("Video downloaded")
    else:
        quit()

    speaker.Speak("Do you want to use Pytuber again")
    use_again = input("Enter Y/y for Yes any other key for No: ")
else:
    quit()