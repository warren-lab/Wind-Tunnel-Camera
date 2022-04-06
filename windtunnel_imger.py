# Final Version of Script in order to run on the wind tunnel
# This program gives the user the option of whether or not to take a certain number of images or do a timelapse of images
from picamera import PiCamera
from time import sleep
from datetime import datetime, timedelta
import os
## have this script be something that is user friendly... let's try to convert this to a class later on...
## so then this can be later utilized as a function and imported to make things easier

# called PiCamera
camera = PiCamera()

# defined function for UI printing:
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


# the path for saving the folders to
path = "/home/pi/Desktop/images/windtunnel_images/Still_Images/"

# next display the function:
print_stats()
## asked user for their option
user_input = int(input())

# then the user enters the while loop with another input
while user_input in range(1,5): # going from 1 to 4
    # follow the below model for an if statement
    # first if statement for user_defined number of images
    if user_input == 1:
        # the path for saving the folders to for the still images
        path = "/home/pi/Desktop/images/windtunnel_images/Still_Images/"
        print(" You are requesting to take X number of images would you like to proceed (y/n)")
        img1_input = input()
        if img1_input == "y":
            camera.resolution = (2592, 1944)
            print("Please enter the number of images you would like to take")
            num_imgs = int(input())
            print("Please specify how much time you want in between images")
            delay_time = int(input())
            # now for taking the x number of images a for loop will be set up to take that many images sequentially..
            for capture in range(1, num_imgs+1):
                # then introduce the file path and include the data and time into this as well..
                time_folder = str(datetime.now().strftime("%Y-%m-%d"))
                ## New path was created to save the images to
                path_new = os.path.join(path,time_folder)
                os.makedirs(path_new, exist_ok = True)
                # location where file will be saved was updated.
                location = path_new + "/%s.jpg"
                # Current time for the file
                time_current = datetime.now().strftime("%H:%M:%S")
                # filename was generated
                filename = location % time_current
                # preview the images...
                camera.start_preview()
                
                
                # Image was saved to file location
                camera.capture(filename)
                
                sleep(delay_time)
                # end the preview
                camera.stop_preview()
                
                
                #pathname = '/home/pi/Desktop/images/windtunnel_images/'+str(capture)+'.jpg'
                #camera.capture(pathname)
            # print_stats(img_input)
        #     # user_init = int(input())
        else:
            # Determine how the user would like to proceed
            print_stats()
            user_input = int(input())
  #   #   #   #   #   #   #   #   #   #   #   
# second condition is if user
###  While within in input 2 there will be no camera preview.
    elif user_input == 2:
        # path to save the images to the timelapse folder
        path = "/home/pi/Desktop/images/windtunnel_images/Timelapse/"
        print("You are requesting to perform a timelapse for X duration, would you like to proceed (y/n)")
        img2_input = input()
        if img2_input == "y":
            camera.resolution = (2592, 1944)
            # set the frame rate
            camera.framerate = 2
            # set the duration
            print("Duration (Enter whole number of minutes)")
            time_min = int(input())
            print("Duration (Enter a whole number of seconds)")
            time_sec = int(input())
           
            # developed the change in time:
            tdelta = timedelta(seconds = time_sec, minutes = time_min)
           
            # set the start time
            start_time = datetime.now()

            # set the folder for the timelapse
            timelapse_folder = str(start_time.strftime("%Y-%m-%d"))
            path_new = os.path.join(path,timelapse_folder)
            os.makedirs(path_new, exist_ok = True)
            # added the the time delta to the before time to get the ending time
            time_end = start_time + tdelta
            ## checking how many images were created...
            #### comment this out when program is successful
            count = 1
            # documented the location for where all of the files will be saved
            ## now in the while loop the images will be added to this path
            location = path_new + "/%s.jpg"
            # now before timelapse starts name it based on
            print("starting the while loop")
            # started a preview so that the user can be able to see the image
            #camera.start_preview()
            while datetime.now() <= time_end:
                # new filename with current time
                #time_current = datetime.now().strftime("%H:%M:%S")
                time_current = datetime.now()
                time_current_split = str(time_current.strftime("%H:%M:%S.%f"))
                filename = location % time_current_split
                # saved the image
                ## set the video port to true in order to enable fast image processing...
                camera.capture(filename, use_video_port = True)
                #camera.capture(filename)
                
                count +=1
            #camera.stop_preview()
            print("count", count)
            frame_rate = count/tdelta.seconds
            print(" frame rate", frame_rate)
            print("end", time_end)
        else:
           # Determine how the user would like to proceed
            print_stats()
            user_input = int(input())
    # this condition is if user would like to view the images...
    elif user_input == 3:
        # calibrate the camera.. sets a camera preview with a command to only stop the preview after the user presses a key
        # make sure the user knows that the following only works when GUI is activated on the Pi
        print("You are requesting to look at the images taken, make sure GUI is enabled in order to do so, proceed (y/n)")
        img3_input = input()
        # add the rest of it...

# last option is to quit the program
if user_input == 4:
    quit() #this will quit the program
