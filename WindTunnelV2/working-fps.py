#!/usr/bin/python3
import time
from datetime import datetime,timedelta

from picamera2 import Picamera2
import os
size = (2304,1296)
lens_position = 4.0

# the path for saving the folders
path_test = "/home/pi/swd_imgs/test/"
path_timelapse = "/home/pi/swd_imgs/"

date_folder = str(datetime.now().strftime("%Y-%m-%d"))

# add folder to the path 
test_path = os.path.join(path_test,date_folder)
os.makedirs(test_path, exist_ok = True)

picam2 = Picamera2()
cam_config = picam2.create_still_configuration({'size': size})
picam2.exposure_mode = 'sports'
picam2.configure(cam_config)
picam2.set_controls({"LensPosition": lens_position})
picam2.start()

# Give time for Aec and Awb to settle, before disabling them
time.sleep(1)

# Framerate limitation -> 1fps or less for now
picam2.set_controls({"AeEnable": False, "AwbEnable": False, "FrameRate": 1})
# And wait for those settings to take effect
time.sleep(1)

current_time = datetime.now().strftime("%y%m%d_%H%M")
timelapse_folder = current_time+'_'+"bob"
timelapse_dat = os.path.join(path_timelapse,timelapse_folder)
os.makedirs(timelapse_dat, exist_ok = True)
# for i in range(1, 61):
time_end = datetime.now() + timedelta(minutes =1)
while datetime.now() <= time_end:
    r = picam2.capture_request()
    r.save("main", timelapse_dat+"test_"+datetime.now().strftime("%H-%M-%S")+'.jpg')
    r.release()
    # print(f"Captured image {i} of 50 at {time.time() - start_time:.2f}s")


picam2.stop()