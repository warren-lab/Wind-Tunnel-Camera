# Wind-Tunnel-Camera
This repository contains the documentation and necessary script for imaging flies within a wind tunnel. The Pi HQ Camera V2 was used along with a Raspberry Pi 4 and necessary PiCamera API.

Latest: WittyTunnel
- Using Pi Camera Module 3
****

SET SPECIFICALLY FOR SWD TRACKING PROJECT

For recording at specific time intervals using Pi camera with Witty Pi

INITIAL SET UP IN MONITOR:

- Connect mouse, keyboard, hdmi connector
  
- Connect battery to the Witty Pi (not the base pi!). Check battery power.
  
- Wait for white flashing light, then press fully black button. the pi is on when the green and red lights are on
  
- If the display does not work, press the black button to restart, if not, then unplug and plug the battery

Otherwise connect through SSH 
To ssh into pi: 

Plug ethernet cbale into pi

From command line in lab computer:
ssh -vvv pi@10.42.0.123

(wait a minute before running commands for internal processes to fully run)

enter flyranch password

On the display:

open the terminal top bar
- check the status of the system:
```
sudo systemctl status windtunnel.service
```
Ctrl +C to exit

then stop it by: 
```
sudo systemctl stop windtunnel.service
```

TO RESET/STOP STARTUP/SHUTDOWN TIMES: 

```
cd wittypi/
```
ls
```
./wittyPi.sh
```

-Option 12 (Reset data)

-Option 1 (clear scheduled startup time)

-Option 12 (Reset data)

-Option 2 (clear scheduled shutdown time)

-Option 13 (Exit)

(next to options 4 and 5 should be clear, no times, means it will not startup at scheduled times or instantly shutdown)

TO SET UP STARTUP/SHUTDOWN SCHEDULER:

Go up one directory
```
cd ../Wind-Tunnel-Camera/WittyTunnel/
```
```
sudo nano config.ini
```

Type experiment name -> ctrl + x 

Change startup and shutdown time if necessary (HH,mm,ss)

Save modified buffer? Y + enter

TO SHUTDOWN PI
```
sudo shutdown -h now
```

Press black button again to reboot (when connected to the battery), it will start recording at the scheduled times. 

TO CHECK STATUS:
```
sudo systemctl status windtunnel.service
```
Check startup and shutdown times (only once camera has been initialized according to status above):

```
cd wittypi/
```
ls
```
./wittyPi.sh
```

Look at times in options 4 and 5. Next shutdown (4) should be in a few minutes, but next startup (5) should be at the closest scheduled time
press 13 to exit

If connected to SSH, type "exit" to leave SSH connection
-----

To calibrate system time:
Option 3 (synchronize with network time)

To change recording times

in wittypi.py

in def shutdown_startup

within the function you can change startup and end times for each interval

***** 	
TO RUN INSTANT TIMELAPSE:

```
cd Wind-Tunnel-Camera/WindTunnelV2
```
```
./run_timelapse.py
```




