# Control Script Service...
This details how the control script runs in background as a systemd service...


After this then tested that it worked properly


Then created the service...
- first created the servce file
```
sudo nano /etc/systemd/system/windtunnel.service
```
- after this point we then can work with the general structure seen in this [tutorial](https://www.thedigitalpictureframe.com/ultimate-guide-systemd-autostart-scripts-raspberry-pi/
```                           
[Unit]
Description=Service file that will start the bee_cam script up
After=network.target datetime_sync.service # after the RTC.service has been completed

[Service]
Type=oneshot
WorkingDirectory=/home/pi/Wind-Tunnel-Camera/
User=pi
ExecStart=/bin/sleep 90
ExecStart=/usr/bin/python3 /home/pi/Wind-Tunnel-Camera/WittyTunnel/control.py
RemainAfterExit=true

[Install]
WantedBy=multi-user.target

```

- now with final completed change the file permission, make sure in right directory
```
sudo chmod 644 windtunnel.service
```
- then reload the daemon

```
sudo systemctl daemon-reload
```

- enable to start on boot

```
sudo systemctl enable windtunnel.service
```

- should be good to go now...

- TESTING:
    - Shutdown/Reboot the pi, and then turn pi back on. At this point wait for several minutes. 

    - After several minutes then we need to essentially stop this service

    - After stopping the service then let us go back to check on this service and what happened with the data collected

    ```
    sudo systemctl stop windtunnel.service
    ```
    - After stopping the service then do a reload/restart of it if everything is okay

    ```
    sudo systemctl reload windtunnel.service
    ```


- IF THERE IS AN ISSUE THEN DISABLE THE SERVICE
```
sudo systemctl disable bee_cam.service
```






IMPORTANT: When changes have been made to the python file you will need to restart the specific service...
```
sudo systemctl reload name-of-your-service.service
```



################### BASH SCRIPT TESTING METHOD#################



nohup python control.py &


