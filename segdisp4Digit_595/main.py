import time
import machine
from machine import SPI, Pin
import segdisp4Digit_595


#NUM_5 is an example of a constant that is declared in the segdisp4Digit Module, to make it easier to display what you want. Refer to the segdisp4Digit Module or the README to know what to type into writeToDisplay().


#Initializes pins that will be used for the display, in order of segments ( A, B, C, D, E, F, G, DP)
vspi = SPI(2, baudrate=80000000, polarity=1, phase=0, bits=8,firstbit=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
segdisp4Digit_595.initPins_4Digit_595(vspi, 14, 12, 13)

#Initializes digit pins that will be used for the 4 digit display, in order of (D1, D2, D3, D4)
segdisp4Digit_595.initDigitPins_4Digit_595(33, 25, 26, 27)

#Runs through all segment display options to test the 4 digit display. Goes through numbers, letters, and special.
#segdisp4Digit.testDisplay_4Digit_595()


while (True):

#Writes to the display numbers, 1, 2, 3, 4.
	
	segdisp4Digit_595.writeToDisplay_4Digit_595(segdisp4Digit_595.NUM_1, segdisp4Digit_595.NUM_2, segdisp4Digit_595.NUM_3, segdisp4Digit_595.NUM_4)	
	








