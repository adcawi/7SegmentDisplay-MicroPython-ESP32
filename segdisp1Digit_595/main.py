import time
import machine
from machine import SPI, Pin
import segdisp1Digit_595

#NUM_1 is an example of a constant that is declared in the segdisp1Digit_595 Module, to make it easier to display what you want. Refer to the segdisp1Digit Module or the README to know what to type into writeToDisplay().


#Initializes pins that will be used for the segment shifter/ display
# in order of  ( SPI OBJECT, RCLCK, OE, CLR)
vspi = SPI(2, baudrate=80000000, polarity=1, phase=0, bits=8, firstbit=0, sck=Pin(18), mosi =Pin(23), miso=Pin(19))
segdisp1Digit_595.initPins_1Digit_595(vspi, 14, 12, 13)

#Tests the display, runs through all visual options.
segdisp1Digit_595.testDisplay_1Digit_595()

#Start of main loop
while (True):
#Writes to the display number 1.
	

	segdisp1Digit_595.writeToDisplay_1Digit_595(segdisp1Digit_595.NUM_1)	
	time.sleep(1)
		
	segdisp1Digit_595.writeToDisplay_1Digit_595(segdisp1Digit_595.LETTER_E)
	time.sleep(1)







