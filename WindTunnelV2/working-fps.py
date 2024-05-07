#!/usr/bin/python3
import time
from datetime import datetime

from picamera2 import Picamera2
size = (2304,1296)
lens_position = 4.0

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
for i in range(1, 61):
    r = picam2.capture_request()
    r.save("main", "test_"+datetime.now().strftime("%H-%M-%S")+'.jpg')
    r.release()
    print(f"Captured image {i} of 50 at {time.time() - start_time:.2f}s")


picam2.stop()