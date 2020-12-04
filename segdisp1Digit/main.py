import time
import machine
import segdisp1Digit

#NUM_5 is an example of a constant that is declared in the segdisp1Digit Module, to make it easier to display what you want. Refer to the segdisp1Digit Module or the README to know what to type into writeToDisplay().


#Initializes pins that will be used for the display, in order of segments ( A, B, C, D, E, F, G, DP)
segdisp1Digit.initPins_1Digit(18, 19, 21, 22, 23, 25, 26, 32)

#Tests the display, runs through all visual options.
segdisp1Digit.testDisplay_1Digit()


#Start of main loop
while (True):

#Writes to the display number 1.
	

	segdisp1Digit.writeToDisplay_1Digit(segdisp1Digit.NUM_1)	
	








