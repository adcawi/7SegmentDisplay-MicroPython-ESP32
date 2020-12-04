import time
import machine
import segdisp4Digit

#NUM_5 is an example of a constant that is declared in the segdisp4Digit Module, to make it easier to display what you want. Refer to the segdisp4Digit Module or the README to know what to type into writeToDisplay().


#Initializes pins that will be used for the display, in order of segments ( A, B, C, D, E, F, G, DP)
segdisp4Digit.initPins_4Digit(18, 19, 21, 22, 23, 25, 26, 32)

#Initializes digit pins that will be used for the 4 digit display, in order of (D1, D2, D3, D4)

segdisp4Digit.initDigitPins_4Digit(0, 15, 4, 5)

#Runs through all segment display options to test the 4 digit display. Goes through numbers, letters, and special.
#segdisp4Digit.testDisplay_4Digit()


while (True):

#Writes to the display numbers, 1, 2, 3, 4.
	
	segdisp4Digit.writeToDisplay_4Digit(segdisp4Digit.NUM_1, segdisp4Digit.NUM_2, segdisp4Digit.NUM_3, segdisp4Digit.NUM_4)	
	








