# Pytuber
I am sure, everyone is a fan of **YouTube** and truly so, for there is everything there, starting from *Entertainment* to *Educational* videos. But it may, at times happen that you don't have access to internet and you immediately need to re-refer to something that you had watched earlier. Well, for that the only good option is that, either you have the videos downloaded in your device, the most important ones; for which either you would have to visit some pages having advertisements all over them and pop-ups opening on click or you may have to download and install some software or application to your device. Who takes that much of an headache, not me, to be true.

_**Pytuber**_ a minimalist application I developed using a little bit of Python scripting serves the purpose for you really well. It doesn't have any crimpy ads nor do you need to install it. Just run the application when needed and close it when task is accomplished.

## Application Overview
This section gives an overview of the project dependencies and the development environment.
### Development Environment
* __Operating System:__ Windows 8.1
* __Architecture:__ 64 bit
* __Development Language:__ Python
* __IDE:__ Pycharm Community Edition 2017.1.5
* __Interpreter:__ Python 3.6.4

### Module Dependencies
* __Beautiful Soup:__ Used for web scraping to obtain the video links to download.
* __Requests:__ To send HTTP/1.1 requests without manual intervention.
* __Pytube:__ To download YouTube videos
* __win32com.client:__ To use the Microsoft Client Side Speech API
* __tkinter:__ To implement GUI

## Installation
If you are a developer, and you want to use the code for modifying it and making your own version of it, then you would have to install a few modules to be able to work with the code; as the modules that I have used don't come by default with Python Installation. The installation and any details that i discuss here are for windows development environment. You can Google out the results for other OS or wait for we to update it here.
In order to install the modules you have to open command prompt in administrator mode (if you have not provided full access to CMD by default).

* Type ```pip install beautifulsoup4``` and press enter to install **BeautifulSoup** or download the proper version from https://pypi.python.org/pypi/beautifulsoup4 

* Type ```pip install requests``` and press enter to install **requests** or visit https://pypi.python.org/pypi/requests and download the module.

* Type ```pip install pytube``` and press enter to install **pytube** or visit https://pypi.python.org/pypi/pytube/ and download the module.

* Type ```pip install pypiwin32``` and press enter to install **win32com** or visit https://pypi.python.org/pypi/pypiwin32 and download the module.
