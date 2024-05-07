#!/usr/bin/python3
import time

from picamera2 import Picamera2
from datetime import datetime, timedelta
import os

size = (2304,1296)
lens_position = 4.0
# the path for saving the folders
path_test = "/home/pi/swd_imgs/test/"
path_timelapse = "/home/pi/swd_imgs/"

date_folder = str(datetime.now().strftime("%Y-%m-%d"))

# add folder to the path 
test_path = os.path.join(path_test,date_folder)
# time_path = os.path.join(path_timelapse, date_folder)
# make the new directories on the path
os.makedirs(test_path, exist_ok = True)

exp_name = "Testing"

picam2 = Picamera2()
cam_config = picam2.create_still_configuration({'size': size})
picam2.exposure_mode = 'sports'
picam2.configure(cam_config)
picam2.set_controls({"LensPosition": lens_position})
picam2.start()

# Give time for Aec and Awb to settle, before disabling them
time.sleep(1)

picam2.set_controls({"AeEnable": False, "AwbEnable": False, "FrameRate": 1.0})
# And wait for those settings to take effect
time.sleep(1)

start_time = time.time()
# set the start time
current_time = datetime.now().strftime("%y%m%d_%H%M")
print(current_time)
start_time = current_time
start_time_new = datetime.strptime(start_time ,"%y%m%d_%H%M")
# set the folder for the timelapse
timelapse_folder = str(start_time)+'_'+exp_name
path_new = os.path.join(path_timelapse,timelapse_folder)
os.makedirs(path_new, exist_ok = True)

# Change working directory to save image files:
print(path_new)
os.chdir(path_new)

# added the the time delta to the before time to get the ending time

time_end = (start_time_new + timedelta(minutes = 1))
print(time_end.strftime("%y%m%d_%H%M"))

while datetime.now() <= time_end:
    r = picam2.capture_request()
    r.save("main", f"test_{datetime.now().strftime("%H-%M-%S")}.jpg")
    r.release()
    print(f"Captured image {i} of 50 at {time.time() - start_time:.2f}s")


picam2.stop()