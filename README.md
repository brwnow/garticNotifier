# Gartic Notifier

Gartic Notifier is an experimental tool which the main functionality is notifying you when your friends login in Gartic. It's a proof of concept that I decided to develop it to gather some practical informations about polling gartic server with continously http requests, in order to better decide if it's worth developing an Android application that notifies the user when its gartic friends login their accounts.

### License

> Copyright © 2020 Bruno Garcia <brwnow@gmail.com>  
> This work is free. You can redistribute it and/or modify it under the  
> terms of the Do What The Fuck You Want To Public License, Version 2,  
> as published by Sam Hocevar. See the COPYING file for more details.  

_________________

## Summary

- [1. Installation](#1-installation)  
  - [1.1. Linux](#11-linux)  
  - [1.2. Windows](#12-windows)  
- [2. Usage basics](#2-usage-basics)

_________________

## 1. Installation

### 1.1. Linux

***TO DO***  

### 1.2. Windows

Download and install [python 3.8.4](https://www.python.org/downloads/release/python-384/)  

Now check this [Adding entry to PATH env Guide](https://docs.alfresco.com/4.2/tasks/fot-addpath.html) and add the path to the folder where you installed python to the `PATH env`  

With the python installation location added to PATH env, install the following libraries to running the commands below in the terminal:

 ```
python -m pip install beautifulsoup4
python -m pip install keyboard
 ```

Now download this repository by clicking **code** at the upper-right corner of this page and then clicking **Download ZIP**  

![Downloading repository](/doc/images/downloadRepo.png?raw=true "Downloading repository")  

_________________

## 2. Usage basics

Open the terminal, navigate to Gartic Notifier folder and call python passing Gartic Notifier entry ponit file `main.py` and pass as the single argument your gartic's username as below  

```
python main.py yourUsernameHere
```  

Then the application will start showing each 60 seconds if any of your friends has logged in Gartic. If any friends has logged in, nothing will be shown  

To quit the application press `Ctrl + Shift + Q` in the terminal window. Sometimes python get stuck performing network requests, so if it get stuck and don't finish the application, close the terminal  

<details>
    <summary>
        Exmaple
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