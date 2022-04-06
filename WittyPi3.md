# Using Witty Pi 3 with Raspberry Pi 4

Reference: https://www.adafruit.com/product/5038

## Setting up Witty Pi
1. Disable 1- Wire Interface
2. Connect the Raspberry Pi to internet
3. Install the software
```
wget http://www.uugear.com/repo/WittyPi3/install.sh
```
4. Then run the following to complete the installation:
```
sudo sh install.sh
```
5. Refer to the documentation and that the proper files are present within the wittypi directory
6. Mount the Witty Pi 3 on to Raspberry Pi, and inset coin cell
7. Then unplug the power to the Pi and only have power go through the WittyPi
8. Running Software:
```
./wittyPi.sh
```
This will display the different options that are available to be performed

## Witty Pi as RTC
1. Make sure that the Pi is connected to the internet
2. Run Software:
```
./wittyPi.sh
```
2. First test the Witty Pi by writing the current time on the Pi to the Witty Pi.
This is done by selecting option 1
```
1
```
3. Determine whether this was successful by running the software again and looking at the output
4. If this is correct then have the RTC write to the system
```
2
```
6. Then switch off internet connection and shutdown the Pi, and wait a minute or two and power on the WittyPi
7. Then check the time to see if it is the current time.
8. If not try this process again and look to see if there is an issue with the coincell.
9. Could also do this process by using synchronize time
```
3
```


