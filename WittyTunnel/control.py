#!/usr/bin/env python3
"""
Short description 
"""

import os
import sys
from wittypi import WittyPi, ShutdownTime
from picamera2 import Picamera2
from time import sleep
from datetime import datetime,timedelta
import configparser

# Experiment Configuration:
config = configparser.ConfigParser()
config.read("config.ini")

# size = (1920,1080)
size = (4608,2592)
# (2304,1296) # 1 fps
lens_position = 4.2
# 4.0 # fps
# 4.2 <- lens_position less blur...
# 5.3 < original lens position

# the path for saving the folders
path_test = "/home/pi/swd_imgs/test/"
path_timelapse = "/home/pi/swd_imgs/"

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
# Give time for Aec and Awb to settle, before disabling them
sleep(1)

# Framerate limitation -> 1fps or less for now
picam2.set_controls({"AeEnable": False, "AwbEnable": False, "FrameRate": 1})
# And wait for those settings to take effect
sleep(1)


    
current_time = datetime.now()
timelapse_folder = current_time.strftime("%y%m%d_%H%M") +'_'+exp_name
timelapse_dat = os.path.join(path_timelapse,timelapse_folder)
os.makedirs(timelapse_dat, exist_ok = True)
# for i in range(1, 61):
time_end = current_time + dur2_delta 
count = 1
while datetime.now() < time_end:
    try:
        r = picam2.capture_request()
        r.save("main", timelapse_dat+"/frame_"+"{:05d}".format(count) +'.png')
        r.release()
        count +=1


    except KeyboardInterrupt:
        if len(list(sensors.data_dict.values())[0]) != 0:
            disp.display_msg('Update CSV', img_count)
            soc, volt = disp.get_batt_charge()
            logging.info(f"Battery Charge (SoC & Volt): {soc}% {volt}%") 
            # if list is not empty then add data...
            sensors.append_to_csv()
            time.sleep(3) 
        
        disp.display_msg('Interrupted', img_count)
        logging.info("KeyboardInterrupt")
        time.sleep(3)
        disp.disp_deinit()
        time.sleep(1)
        sensors.sensors_deint()
        sys.exit()
    except DarkPeriod:
        if len(list(sensors.data_dict.values())[0]) != 0:
            disp.display_msg('Update CSV', img_count)
            soc, volt = disp.get_batt_charge()
            logging.info(f"Battery Charge (SoC & Volt): {soc}% {volt}%") 
            # if list is not empty then add data...
            sensors.append_to_csv()
            time.sleep(3)  
        disp.display_msg('Dark Period Shutdown', img_count)

        logging.info("DarkPeriod")
        with WittyPi() as witty:
            # print("Shutdown Time")
            witty.shutdown()
            witty.startup()
        time.sleep(3)
        disp.disp_deinit()
        time.sleep(1)
        sensors.sensors_deint()
        sys.exit()

    except ShutdownTime:
        if len(list(sensors.data_dict.values())[0]) != 0:
            disp.display_msg('Update CSV', img_count)
            soc, volt = disp.get_batt_charge()
            logging.info(f"Battery Charge (SoC & Volt): {soc}% {volt}%") 
            # if list is not empty then add data...
            sensors.append_to_csv()
            time.sleep(3)
        
        disp.display_msg('Timed Shutdown', img_count)
        
        with WittyPi() as witty:
            # print("Shutdown Time")
            witty.shutdown()
            witty.startup()
        time.sleep(3)
        disp.disp_deinit()
        time.sleep(1)
        sensors.sensors_deint() 
        sys.exit()

    except TimeoutError:
        retry_count += 1
        disp.display_msg('Cam Timeout!', img_count)
        logging.error("Camera operation timeout!")
        if retry_count >= MAX_RETRIES:
            disp.display_msg('Max retries reached!', img_count)
            soc, volt = disp.get_batt_charge()
            logging.info(f"Battery Charge (SoC & Volt): {soc}% {volt}%")
            logging.error("Max retries reached. Exiting...") 
            with WittyPi() as witty:
                # print("Shutdown Time")
                witty.shutdown()
                witty.startup()
            time.sleep(3)
            disp.disp_deinit()
            time.sleep(1)
            sensors.sensors_deint() 
            sys.exit()
        else:
            # Wait for a bit before attempting a retry
            sleep(2)
            continue
    except:
        disp.display_msg('Error', img_count)
        soc, volt = disp.get_batt_charge()
        logging.info(f"Battery Charge (SoC & Volt): {soc}% {volt}%")
        logging.exception("Error capturing image")
        time.sleep(3)
        disp.disp_deinit()
        time.sleep(1)
        sensors.sensors_deint()
        sys.exit()

