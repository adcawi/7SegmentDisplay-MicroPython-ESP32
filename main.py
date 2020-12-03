import time
import machine
import segdisp1Digit

#NUM_5 is an example of a constant that is declared in the segdisp1Digit Module, to make it easier to display what you want. Refer to the segdisp1Digit Module or the README to know what to type into writeToDisplay().


#Initializes pins that will be used for the display, in order of segments ( A, B, C, D, E, F, G, DP)
segdisp1Digit.initPins_1Digit(18, 19, 21, 22, 23, 25, 26, 32)

#Runs through all segment display options to test the 1 digit display. Goes through numbers, letters, and special.
segdisp1Digit.testDisplay_1Digit()

time.sleep(1)

#Writes to the display number 5.	
segdisp1Digit.writeToDisplay_1Digit(segdisp1Digit.NUM_5)	

time.sleep(0.5)

#Writes to the display letter A.
segdisp1Digit.writeToDisplay_1Digit(segdisp1Digit.LETTER_A)	

time.sleep(0.5)

#Writes to the display a horizontal lines visual.
segdisp1Digit.writeToDisplay_1Digit(segdisp1Digit.HORIZONTAL_LINES)


