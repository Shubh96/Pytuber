# How Pytuber works
## Downloading single video
**LINE 2:** ```from pytube import YouTube``` imports the necessary modules for connecting to YouTube via the video URL.

**LINE 17:** ```yt_object = YouTube(download_url)``` creates an object of the YouTube class corresponding to the download_url which is the URL of the video to be downloaded.

**LINE 18:** ```dl_video_stream = yt_object.streams.first()``` this assignment is a two step process. First, ```yt_object.streams``` returns all the various streams that are available for the video to be downloaded. Next, out of those streams, the first stream is selected for download (as the first one has the best resolution). So now, ```dl_video_stream``` has the video details.

**LINE 21:** ```dl_video_stream.download(download_location)``` is one of the several tasks that can be performed. This statement starts the video download and saves the video into the download_location.
