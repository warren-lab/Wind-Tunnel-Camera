#!/usr/bin/env python3
"""
Short description 
"""

import os
import sys
import logging
from wittypi import WittyPi, ShutdownTime
from picamera2 import Picamera2
from time import sleep
from datetime import datetime,timedelta
import configparser

# Experiment Configuration:
config = configparser.ConfigParser()
config.read("config.ini")
exp_name = config['experiment']['name']
# size = (1920,1080)
size = (4608,2592)
# (2304,1296) # 1 fps
lens_position = 5.3
# 4.0 # fps
# 4.2 <- lens_position less blur...
# 5.3 < original lens position

# the path for saving the folders
path_test = "/home/pi/swd_imgs/test/"
path_timelapse = "/home/pi/swd_imgs/"
current_time = datetime.now()
timelapse_folder = current_time.strftime("%y%m%d_%H%M") +'_'+exp_name
timelapse_dat = os.path.join(path_timelapse,timelapse_folder)
os.makedirs(timelapse_dat, exist_ok = True)

# initialize wittypi shutdown
with WittyPi() as witty:
    shutdown_dt = witty.shutdown_startup()
    # witty.startup() # initialize the startup incase something happens...

log_file = timelapse_dat + "/log.txt"
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Initializting Camera....")
# Camera Initalization
try:
    picam2 = Picamera2()
    # prev_config = picam2.create_preview_configuration()
    # picam2.configure(prev_config)
    cam_config = picam2.create_still_configuration({'size': size})
    picam2.exposure_mode = 'sports'
    picam2.configure(cam_config)
    # prev_config = picam2.create_preview_configuration()
    # picam2.configure(prev_config)
    picam2.set_controls({"LensPosition": lens_position})
    picam2.start()
    sleep(5)
except:
    logging.error("Camera initialization failed")
    sys.exit()
# Give time for Aec and Awb to settle, before disabling them
sleep(1)
# Framerate limitation -> 1fps or less for now
picam2.set_controls({"AeEnable": False, "AwbEnable": False, "FrameRate": 1})
# And wait for those settings to take effect
sleep(1)

# Start Experiment
logging.info("###################### Starting Experiment ######################")
sleep(3)
count = 1
while True:
    try:
        r = picam2.capture_request()
        r.save("main", timelapse_dat+"/frame_"+"{:05d}".format(count) +'.png')
        r.release()
        count +=1
        if shutdown_dt <= datetime.now():
            raise ShutdownTime
        
    except KeyboardInterrupt:
        logging.info("KeyboardInterrupt")
        sleep(3) 
        sys.exit()

    except ShutdownTime:
        with WittyPi() as witty:
            # print("Shutdown Time")
            witty.shutdown()
            
        sleep(3)
        sys.exit()
        
    except:
        logging.exception("Error capturing image")
        sys.exit()

