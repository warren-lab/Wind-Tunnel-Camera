#!/usr/bin/env python3

import os
import sys
import logging
from picamera2 import Picamera2
from time import sleep, perf_counter
from datetime import datetime,timedelta
def print_stats():
    print('''
    =========================================
    =========================================
            Options for imaging           
    =========================================
    Please input an integer value from 1-3,
    or press 4 to display more options     
    =========================================
    =========================================
        1. User Defined Number of Images   
        2. Timelapse Images for Duration   
        3. UNDER CONSTRUCTION                                 
        4. Quit Program                    
    =========================================
    ''')
# defined function for getting timelapse start time 
def get_time():
    """ This function will get the current time when requested by the user"""
    time = datetime.now()
    time_of_release = time.strftime("%Y-%m-%d %H:%M:%S")
    return time_of_release


size = (2304,1296)
lens_position = 4.0

# the path for saving the folders
path_test = "/home/pi/swd_imgs/test/"
path_timelapse = "/home/pi/swd_imgs/"

date_folder = str(datetime.now().strftime("%Y-%m-%d"))

# add folder to the path 
test_path = os.path.join(path_test,date_folder)
time_path = os.path.join(path_timelapse, date_folder)
# make the new directories on the path
os.makedirs(test_path, exist_ok = True)
os.makedirs(time_path, exist_ok = True)


camera = Picamera2()
cam_config = camera.create_still_configuration({'size': size})
camera.configure(cam_config)
camera.exposure_mode = 'sports'
camera.set_controls({"AeEnable": False, "AwbEnable": False, "FrameRate": 1.0, "LensPosition": lens_position})
camera.start()
sleep(5)

# print(print_stats())
# user_input = int(input())
if sys.argv[1] == "-t":
    try:
        delay_time = 120
        location = test_path + "/Pi1_%s.jpg"
        # Current time for the file
        time_current = datetime.now().strftime("%Y%m%d%_H%M%S")
        # filename was generated
        filename = location % time_current

            
        # Image was saved to file location
        camera.capture_file(filename)
                        
        sleep(delay_time)

    except KeyboardInterrupt:
        print("Interrupt")
  #   #   #   #   

elif sys.argv[1] == "-r":
    # developed the change in time:
        tdelta = timedelta(minutes = 1)
        # set the start time
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        print(current_time)
        start_time = current_time
        start_time_new = datetime.strptime(start_time ,"%Y%m%d%H%M%S")
        # set the folder for the timelapse
        timelapse_folder = "Pi1_"+str(start_time)
        path_new = os.path.join(time_path,timelapse_folder)
        os.makedirs(path_new, exist_ok = True)
        
        # Change working directory to save image files:
        os.chdir(path_new)

        # added the the time delta to the before time to get the ending time
        time_end = (start_time_new + tdelta)
        print(time_end.strftime("%Y%m%d%H%M%S"))
        # start = perf_counter()
        count = 0
        while datetime.now() <= time_end:
            time_current = datetime.now()
            r=camera.capture_request()
            time_current_split = str(time_current.strftime("%Y%m%d_%H%M%S"))
            r.save('Pi1_'+time_current_split+'.jpg')
            r.release()
            count+=1
            sleep(.5)
        print(count)
            # 
        # end=perf_counter()
        # frmerte = count/(end-start)
        # print("Frame Rate:", frmerte)


# Change working directory to save image files:
# os.chdir(time_path)
# print('Imaging')
# logging.info("Imaging...")

# while True:
#     time_current = datetime.now()
#     time_current_split = str(time_current.strftime("%Y%m%d_%H%M%S"))
#     try:
#         camera.capture_file(name + '_' + time_current_split + '.jpg')
#         logging.info("Image acquired: %s", time_current_split)
#         sleep(1)
#     except KeyboardInterrupt:
#         logging.info("Exiting")
#         sys.exit()
#     except:
#         logging.exception("Error capturing image")