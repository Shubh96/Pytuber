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
In order to install the modules you have to open command prompt in administrator mode (if you have not provided full access to CMD by default). But before heading forward to install any module, make sure you have the *__python package manager__* viz a viz **pip** installed in your system. You can check that by typing ```pip --version``` in command prompt and it will show you the version installed (if you have any). If you don't have it then see [Getting pip installed](https://pip.pypa.io/en/stable/installing/).Once you have pip installed, you can continue with the steps below.

* Type ```pip install beautifulsoup4``` and press enter to install **BeautifulSoup** or download the proper version from https://pypi.python.org/pypi/beautifulsoup4 

* Type ```pip install requests``` and press enter to install **requests** or visit https://pypi.python.org/pypi/requests and download the module.

* Type ```pip install pytube``` and press enter to install **pytube** or visit https://pypi.python.org/pypi/pytube/ and download the module.

* Type ```pip install pypiwin32``` and press enter to install **win32com** or visit https://pypi.python.org/pypi/pypiwin32 and download the module.

## Usage
If you want to use my project not for any development purpose but for downloading videos then there are two obvious ways to it. First is you can directly contact me and I can send you the executable along with the necessary files for the project to run. The second method is that you copy the entire source code (the latest version of course) and save it as a python file. Then you can convert it into an executable as described below.

### Making executable file from python script
There are several ways to convert a python script into an executable. I shal briefly describe only few of them here.
#### Using py2exe
First of all, in order to use this method you must have **Python 3.4** or below; as py2exe is not currently compatible with versions higher than that. Also ensure that you have the environment variable set for python.
1. __Installing the py2exe module:__ Run command prompt in administrator mode and type ```pip install py2exe``` and press enter. This will install py2exe in your system.
2. __Writing the setup script:__ Go to the location where you have you *.py* file made which you tend to convert to *.exe*.  In the same location you create one more file named **setup.py** and put the code below into that setup.py file.
```
from distutils.core import setup
import py2exe
setup(console=['filename.py'])
```
Here **_filename.py_** is the .py file you want to convert to exe.
3. __Final step:__ Open command prompt in administrator mode and type ```python setup.py py2exe``` and press enter. This will get your exe file made.

#### Using pyinstaller
Pyinstaller is what I have used to convert my python script into executable file. It also has a lot of options to work around with. Just follow the steps as mentioned below to convert you file into an exe.
1. __Installing the pyinstaller module:__ Run command prompt in administrator mode and type ```pip install pyinstaller``` and press enter. This will install pyinstaller in your system.
2. __Converting into excutable:__ Go to the location where you have you *.py* file made which you tend to convert to *.exe*.  Open command prompt in administrator mode here and type ```pyinstaller filename.py``` for basic executable file. It will convert you script into executable and that you can find inside **dist** folder.
3. __Adding icon to executable:__ If you want to add an icon to you executable then first put the icon in the same folder as the script. Now, type ```pyinstaller filename.py --icon IconFile.ico```. Here IconFile.ico is the icon file.
4. __Creating a single file:__ If you wish to have all the dependencies and packages compressed and built into a single exe file then use ```pyinstaller --onefile filename.py```. This will create only one executable file and nothing else. Doing this would make your application a little slower details of which you can find [here](https://pythonhosted.org/PyInstaller/operating-mode.html#how-the-one-file-program-works)
5. __Creating a single directory:__ Even by default, the pyinstaller creates one folder into which all files are included. But, if you want to do that using some options then you can type ```pyinstaller --onedir filename.py```. This will make no difference to the speed at which you application runs. Details of this you can find [here](https://pythonhosted.org/PyInstaller/operating-mode.html#bundling-to-one-folder)
 
 If you wish to use several options together then you can do that by separating them with spaces like ```pyinstaller --option1 --option2``` and so on.
