# Windtunnel Script User Guide

## Getting Started
(https://picamera.readthedocs.io/en/release-1.13/)
1. If Witty Pi is not attached to the Raspberry Pi, then refer to prior documentation illustrating how this is performed, and how to operate the Pi with the Witty Pi
2. Make sure that power is connected to the Witty Pi ONLY, and connect the pi to the monitor.
3. Check that the time on the Pi is the correct time, if not refer to the Witty Pi documentation for tips on troubleshooting
4. Double click on the Wind Tunnel Imager to start the program
  * For future reference on creating desktop shorcuts the steps for this process can be seen in a section below.
5. Follow the instructions on the UI and proceed accordingly based on how you would like to take images.
  * it is recommended to use the user defined number of images option as a method for focusing the camera. 
## Creation of Desktop Shortcut
Reference: https://www.hackster.io/kamal-khan/desktop-shortcut-for-python-script-on-raspberry-pi-fd1c63

1. Created a text file on the desktop 
> Make sure to save the file to the desktop. And provide your desired name
3. Inputted the following..
```
[Desktop Entry]
Type=Application
NAME= [name that will be displayed on desktop]
Encoding=UTF-8
Exec=python3 [path to python script]
Icon= [path to image]
StartupNotify=true
Terminal=true
```
3. After this point the python script was made an executable
```
chmod +x [path to python file]
```
4. The Desktop Shorcut can then be run 
5. If there is an error with changing the name of the Desktop Shortcut remake it by repeating steps 1-4

