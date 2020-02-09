# color-mixer

Color mixer is a client to be used with Rasberry PI connected to RGB led

## Preparing the Rasberry PI 2 for LED software

Instructions on this can be also found from: https://www.raspberrypi.org/documentation/installation/installing-images/README.md

1. Download Rasbian Buster Lite from rasberrypi.org: https://www.raspberrypi.org/downloads/raspbian/

2. Extract the image file from the package

3. Connect the Rasberry PI SD card to a computer with SD card reader

4. Download https://www.balena.io/etcher/ and use it to flash the extracted Rasbian image file to the SD card

5. Power on the Rasberry PI and hook it up to a monitor, keyboard

6. Default username/password is pi/raspberry. Change the password on the first login using the linux builtin `passwd`-command.

7. Run raspi-config, go to Interfacing options and enable ssh.
Make a note of the IP address for the device if you can't retrieve it from router later

8. Shutdown the Rasberry PI and hook it to local network using the ethernet connection. Remove monitor and keyboard. Connect to it using ssh with
the IP adress you made note of or find it from the router.

```sudo shutdown -P now```

## Enabling GPIO with I2C 

I2C is a serial protocol for embedded systems developed by Philips and used by most of IC manufacturers. It connects
low-speed devices like microcontrollers and other similar peripherals in embedded systems.

Ansible module in this project will install and load two Kernel modules to enable Rasberry PI I2C adapters

* i2c_bcm2708, The low level driver for I2C
* i2c_dev, provides the higher level /dev-access for all of the i2c adapters: https://www.kernel.org/doc/Documentation/i2c/dev-interface
    * Each registered adapter gets assigned with number starting from 0
    * List adapters using i2cdetect -l  

Ansible module also contains required Rasberry Pi configuration to enable (see config.txt.j2) 
    * i2c1
        * TBD
    * spi
        * TBD
    * audio
        * TBD
