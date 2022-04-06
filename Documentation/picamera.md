# **Pi HQ Camera**

It is important to note that due to the most recent update of the Raspberry Pi OS to Bullseye, this has led to many of the prior commands utilzied to communicate with the camera unusable. Although there is a new method for command line interfacing, it would seem that the PiCamera python library has been phased out entirely meaning that in Bullseye communicationwith the camera can only be done through the terminal.

This document will provide methods for how to utilze Bullseye in order to take images with the Pi Camera, and how to get the old Buster OS along with the wifi capabilities. The documentation for the section regarding the Buster version will go into detail on using both command line as well as python programming interfacing with the camera.


## Using Camera with Bullseye
Bullseye uses a new libcamera stack. It is important to note that this should be primarily used with Pi 4's, whereas the Pi zeros and Pi 3's will likely run better with the Buster camera methods.
There are **NO** **Python Bindings available** for this version of the Raspberry Pi OS.

There are different applications that can be accessed via the libcamera-apps
- *libcamera-hello* A simple "hello world" application which starts a camera preview stream and displays it on the screen.

- *libcamera-jpeg* A simple application to run a preview window and then capture high resolution still images.

- *libcamera-still* A more complex still image capture application which emulates more of the features of raspistill.

- *libcamera-vid* A video capture application.

- *libcamera-raw* A basic application for capturing raw (unprocessed Bayer) frames directly from the sensor.

- *libcamera-detect* This application is not built by default, but users can build it if they have TensorFlow Lite installed on their Pi. It captures JPEG images when certain objects are detected.
### Looking at ```libcamera-hello```
##### First perform a check in the command line to ensure everything is running properly:
```libcamera-hello ``` 
This line will start the camera and display a preview window for a few seconds

##### Next try the -t duration option
```libcamera-hello -t **0**```
This allows the user to input whatever they desire for 0 as the duration in miliseconds that the image will be displayed

##### The Tuning File

**Review this**

### Looking at libcamera-jpeg
This captures still images
##### Full resolution JPEG image
```libcamera-jpeg -o test.jpg```
This saves the image to test.jpg

##### Changing duration in preview window, and width and height 
Like the previous libcamera-hello the duration for viewing can be changed so the imaged can remain in the preview window for a longer period.
The width and height cange the resolution of the captured image
```libcamera-jpeg -o test.jpg -t 2000 --width 640 --height 480```

### Looking at ```libcamera-still```
Again this captures a single still image
However, this method also allows for the ability for timelapse to be captured..

##### Standard still image
```libcamera-still -o test.jpg```

##### Change the quality of the image..
100 is the max and 93 is the default 
Only for JPEG use
--quality,	-q		JPEG quality <number>
```libcamera-jpeg -o test.jpg -q 80```


## Using Camera with Buster
When using the picamera with Buster Thonny can be used to develop python scripts. See the below documentation for what sort of commands can be used. 

### Enabled or Disabled the CommandLine or GUI
- Disable GUI
    ```sudo raspi-config```
    Went into the systems options. Then changed the boot so that it boots to the command line with the autologin
    Rebooted the pi
    
- Enable GUI
    ```sudo raspi-config```
    Same steps as above, except need to make sure that enable auto login for desktop
    Rebooted using:
        ```sudo reboot```
    
    
### Using the Command Prompt to Call Python Scripts
- first need to go inside the folder that holds the python scripts
    ```cd Desktop/pythonfiles```
- next referenced python3 and then stated the name of the file in question
  ```python 3 [insert file name here]```
  current files in use:
    * photo_still_time.py
      * This is used for the taking from one to multiple still photos
    * asdf
      * This is used for taking as many as the user desires based on their input instead of taking the all successively at once.
      * This is a manual input one
    * Timelapse
      * This records all of the photos in the form of a timelapse...
    * 
      * Short video every ---minutes...
  

## Sources:
[Raspberry Pi Camera Doc](https://www.raspberrypi.com/documentation/accessories/camera.html)
[More Command Line Documentation](https://www.raspberrypi.com/documentation/accessories/camera.html#common-command-line-options)
[Documentation for PiCamera API](https://picamera.readthedocs.io/en/release-1.13/recipes1.html#capturing-timelapse-sequences)

