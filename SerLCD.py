#import the Circuit Python board and busio libraries
import board
import busio

#enable SPI communications
import digitalio
from sparkfun_serlcd import Sparkfun_SerLCD_SPI

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)

#Setup chip select, CE0
cs = digitalio.DigitalInOut(board.CE0)
cs.direction = digitalio.Direction.OUTPUT

#Create an object for the SerLCD
#As you can see below serlcd has many commands to work with the SerLCD module
serlcd = Sparkfun_SerLCD_SPI(spi, cs)

#Initalization Done

#Clear Display
serlcd.clear()

#Set Backlight RGB to Cyan
serlcd.set_backlight_rgb(0,245,100)
serlcd.write("LCD working with\nthe pi")
