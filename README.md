# Gartic Notifier

Gartic Notifier is an experimental tool which the main functionality is notifying you when your friends login to Gartic. It's a proof of concept that I decided to develop in order to gather some practical informations about polling gartic server with continously http requests, so I can better decide if it's worth developing an Android application that notifies the user when its gartic friends login their accounts.

### License

> Copyright © 2020 Bruno Garcia <brwnow@gmail.com>  
> This work is free. You can redistribute it and/or modify it under the  
> terms of the Do What The Fuck You Want To Public License, Version 2,  
> as published by Sam Hocevar. See the COPYING file for more details.  

## Summary

- [1. Installation](#1-installation)  
  - [1.1. Linux](#11-linux)  
  - [1.2. Windows](#12-windows)  
  - [1.3. Common steps](#13-common-steps)
- [2. Usage basics](#2-usage-basics)

## 1. Installation

As this project was develop and tested only for Python 3 it's recommended that you use Python 3 to run it. If you want to use Python 2, do it on our own risk  

### 1.1. Linux

Follow this [how to install python 3 on ubuntu guide](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu) (if you use another linux distro you probably already have python installed or at least can find your own way on installing python)  

Open the terminal and install python-pip and all Gartic Notifier needed libs by running the following commands:

```
sudo apt install python-pip
pip install beautifulsoup4
pip install keyboard
pip install playsound

```

### 1.2. Windows

Download and install [python 3.8.5](https://www.python.org/ftp/python/3.8.5/python-3.8.5.exe)  

Now check this [Adding entry to PATH env Guide](https://docs.alfresco.com/4.2/tasks/fot-addpath.html) and add the path to the folder where you installed python to the `PATH env`  

<details>
    <summary>
        Do you need some help finding out python installation location?
    </summary>

1. Open start menu and search for "python"
2. Right click the python item in menu and click "Open File Location"
3. It will probably open a folder with a shortcut to python real installation location. Right click the selected shortcut and click "Open File Location"
4. Now you are at the real python istallation location, click the path bar and Ctrl + C the path to this folder

</details>

With the python installation location added to PATH env, open windows terminal (`windows key` + R, then type `cmd` and press enter) and install the following libraries by running the commands below in the terminal:

 ```
python -m pip install beautifulsoup4
python -m pip install keyboard
python -m pip install playsound
 ```

### 1.3. Common steps

Now download this repository by clicking **code** at the upper-right corner of this page and then clicking **Download ZIP**  

![Downloading repository](/doc/images/downloadRepo.png?raw=true "Downloading repository")  

## 2. Usage basics

Open the terminal, navigate to Gartic Notifier folder and call python passing Gartic Notifier entry ponit file `main.py` and also pass your gartic username as below  

```
python main.py yourUsernameHere
```  

Then the application will start showing each 60 seconds if any of your friends has logged in to Gartic. If no friends has logged in, nothing will be shown  

To quit the application press `Ctrl + Shift + Q` in the terminal window. Sometimes python get stuck performing network requests, so if it get stuck and don't finish the application, close the terminal  

<details>
    <summary>
        Example
    </summary>

    C:\Users\brwno\Documents\Projetos\garticNotifier>python main.py _comunicado_
    [01:52:35] | isaafab
    [01:53:35] | itneto_ | rod_mito
    [01:54:35] | docinho_azedo0 | rafa_feroz | apriscmr
    [01:55:35] | gokublack6737
    [01:56:35] | rod_mito
    [01:57:35] | thor_____ | k1r1gaya_
    [01:58:35] | leonardofernandezz | kelgd20 | yournightmare3

</details>
