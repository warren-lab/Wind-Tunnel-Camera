#!/usr/bin/env python3

import os
import sys
import logging
import yaml
from picamera2 import Picamera2
from time import sleep
from datetime import datetime,timedelta
size = (2304,1296)
lens_position = 4.0
name = 'bob'
camera = Picamera2()
cam_config = camera.create_still_configuration({'size': size})
camera.configure(cam_config)
camera.exposure_mode = 'sports'
camera.set_controls({"LensPosition": lens_position})
camera.start()
sleep(5)

# set output dir
path_images = "/home/pi/imaging/images/"
date_folder = str(datetime.now().strftime("%Y-%m-%d"))
time_path = os.path.join(path_images, date_folder)
os.makedirs(time_path, exist_ok=True)

# Change working directory to save image files:
os.chdir(time_path)
print('Imaging')
logging.info("Imaging...")
time_end = datetime.now()+timedelta(minutes = 1)

while datetime.now() <= time_end:
    time_current = datetime.now()
    time_current_split = str(time_current.strftime("%Y%m%d_%H%M%S"))
    try:
        camera.capture_file(name + '_' + time_current_split + '.jpg')
        logging.info("Image acquired: %s", time_current_split)
        sleep(1)
    except KeyboardInterrupt:
        logging.info("Exiting")
        sys.exit()
    except:
        logging.exception("Error capturing image")