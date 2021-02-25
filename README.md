# RasPi-SerLCD
Code to interface a Raspberry Pi with a Spark Fun SerLCD (SPI)


# Install Dependencies

The first step is to enable the hardware SPI which increases the speed of the communication, in the terminal run:

`
sudo raspi-config
`


This will open a menu in the terminal, navigate to Interface Options, and enable SPI. Once this is done we can exit this menu and reboot the pi. Next we need to update the Pi:

`
sudo apt-get update
`

`
sudo apt-get upgrade
`


The next step is to update python tools:

`
sudo pip3 install --upgrade setuptools
`


Now we will install the python libraries:

`
pip3 install RPI.GPIO
`

`
pip3 install adafruit-blinka
`

`
sudo pip3 install sparkfun-circuitpython-serlcd
`

The Pi now has all the needed Libraries.

# Connecting the Rasperry Pi to the SerLCD

Let's start with the power connection, the version of the SerLCD we are testing can handle 3.3V to 9V. So connect either 3.3V or 5v from the Pins on the Pi to the *RAW* power
input of the SerLCD. Connect the GND on the Pi to the GND beside the *RAW* in. Now we connect the SPI of the PI to the LCD.

Make the Following Connections:

Pi ---> LCD

SCLK -> SCK

CE0 --> /CS

MISO -> SDO

MOSI -> SDI


Once these connections have been made, you can now run the .py file in this repo to test and play with the LCD.


### Source
This was developed following this tutorial: https://pypi.org/project/sparkfun-circuitpython-serlcd/
