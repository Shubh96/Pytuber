# How Pytuber works
This documentation gives a description about how this project works. It has been divided into three parts viz a viz *Downloading single video*, *Downloading a playlist* and *Handling Exceptions* in the code.
## Downloading single video
**LINE 2:** ```from pytube import YouTube``` imports the necessary modules for connecting to YouTube via the video URL.

**LINE 17:** ```yt_object = YouTube(download_url)``` creates an object of the YouTube class corresponding to the download_url which is the URL of the video to be downloaded.

**LINE 18:** ```dl_video_stream = yt_object.streams.first()``` this assignment is a two step process. First, ```yt_object.streams``` returns all the various streams that are available for the video to be downloaded. Next, out of those streams, the first stream is selected for download (as the first one has the best resolution). So now, ```dl_video_stream``` has the video details.

**LINE 21:** ```dl_video_stream.download(download_location)``` is one of the several tasks that can be performed. This statement starts the video download and saves the video into the download_location.

## Downloading playlist
**LINE 41:** ```html_doc = requests.get(pl_link).text``` this assignment is also a 2 step process. First, ```requests.get(pl_link)``` sends a HTTP/1.1 request to the *__pl_link__* then the entire text from that page is extracted and stored into *__html_doc__*.

**LINE 42:** ```parsed_doc = BeautifulSoup(html_doc, 'html.parser')``` is used to create a parsed object of the [BeautifulSoup class](https://www.crummy.com/software/BeautifulSoup/bs4/doc/). It first converts the html_doc into UNICODE and then parses the html_doc.

**LINE 43:** ```playlist_anchor = parsed_doc('a', {'class': 'pl-video-title-link'})``` this assignment is based on the CSS understanding. Here, all those links are fetched from the *__parsed_doc__* in which the class attribute of the anchor tag(<>) has been specified as ```pl-video-title-link```.

**LINES 45-46:** This code segment also serves the same purpose as LINE 43 but for a different page which also has the playslist set.
```
if len(playlist_anchor) == 0:
  playlist_anchor = parsed_doc('a', {'class': 'playlist-video'})
``` 

## Handling Exceptions
**LINE 22:** ```except RegexMatchError``` is an exception which is generated if the video URL entered to be downloaded is not correct. This exception is raised by the Pytube module and in order to handle it I have imported pytube.exceptions. If this exception is encountered then the user will be asked to enter the proper URL of a YouTube video again.

**LINE 54:** ```except (HTTPError,  ProxyError, MissingSchema, InvalidURL, ConnectionError, Timeout, URLRequired, TooManyRedirects, InvalidSchema)``` is used to handle the exceptions that get thrown by the ```requests.get(URL)``` method. There can be several exceptions and as of now all have been handled at once in general, which asks the user to enter a proper YouTube playlist URL. For instance if we enter any invalid URL then an HTTP excepton is raised because the request cannot be sent via the HTTP/1.1 protocol where 1.1 specifies the protovcol version.
