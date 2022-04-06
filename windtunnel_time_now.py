# Getting the Current Time Before Running Imager Script
import numpy as np
from datetime import datetime
def get_time():
    """ This function will get the current time when requested by the user"""
    time = datetime.now()
    time_of_release = time.strftime("%Y-%m-%d %H:%M:%S")
    return time_of_release
print(" does user want to take an image")
#user_response = input()
num_counts = 20
empty_array = np.empty(num_counts)
# for i in np.arange(num_counts):
#     try:
#         while True:
#             empty_array[i] = i
#     except KeyboardInterrupt:
#         print(" Pressing Ctr-C to terminate the statememt.")
#         print("Hello World")
#         continue



a = get_time()
print(a)