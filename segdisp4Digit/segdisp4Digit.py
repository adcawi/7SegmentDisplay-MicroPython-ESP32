import machine
import time


#Below are variables used to write to the 1 digit display. A binary string represents which of the 8 segments/pins is high or low, depending on what letter, number, or special visual you want.

#UPPERCASE LETTERS 

LETTER_A =   0b11101110  
LETTER_C =   0b10011100  
LETTER_E =   0b10011110  
LETTER_F =   0b10001110  
LETTER_H =   0b01101110  
LETTER_L =   0b00011100  
LETTER_I =   0b00001100  
LETTER_O =   0b11111100  
LETTER_P =   0b11001110  
LETTER_S =   0b10110110  
LETTER_G =   0b10111110  
LETTER_J =   0b01111000  
LETTER_U =   0b01111100  


#LOWERCASE LETTERS


LETTER_b =   0b00111110  
LETTER_c =   0b00011010  
LETTER_d =   0b01111010  
LETTER_h =   0b00101110  
LETTER_n =   0b00101010  
LETTER_o =   0b00111010  
LETTER_r =   0b00001010  
LETTER_u =   0b00111000  
LETTER_y =   0b01110110  

#Array for testing purposes

letters = [LETTER_A, LETTER_C, LETTER_E, LETTER_F, LETTER_H, LETTER_L, LETTER_I, LETTER_O, LETTER_P, LETTER_S, LETTER_G, LETTER_J, LETTER_U, LETTER_b, LETTER_c, LETTER_d, LETTER_h, LETTER_n, LETTER_o, LETTER_r, LETTER_u, LETTER_y]

#NUMBERS

NUM_0 =   0b11111100  
NUM_1 =   0b01100000  
NUM_2 =   0b11011010  
NUM_3 =   0b11110010  
NUM_4 =   0b01100110  
NUM_5 =   0b10110110  
NUM_6 =   0b10111110  
NUM_7 =   0b11100000  
NUM_8 =   0b11111110  
NUM_9 =   0b11110110  


#Array for testing purposes

numbers = [ NUM_0, NUM_1, NUM_2, NUM_3, NUM_4, NUM_5, NUM_6, NUM_7, NUM_8, NUM_9]

#SPECIAL

BLANK =   0b00000000  
DP =   0b00000001  
VERTICAL_LINES =   0b01101100  
HORIZONTAL_LINES =   0b10010010  
TOP_LINE =   0b10000000  
MIDDLE_LINE =   0b00000010  
BOTTOM_LINE =   0b00010000  
TOP_VERTICAL_LINES =   0b01000100  
BOTTOM_VERTICAL_LINES =   0b00101000  
LEFT_VERTICAL_LINES =   0b00001100  
RIGHT_VERTICAL_LINES =   0b01100000  
TOP_BOTTOM_LINES =   0b10010000  
TOP_MIDDLE_LINES =   0b10000010  
MIDDLE_BOTTOM_LINES =   0b00010010  
ALL_SEGMENTS =   0b11111111  

#Array for testing purposes

special = [BLANK, DP, VERTICAL_LINES, HORIZONTAL_LINES, TOP_LINE, MIDDLE_LINE, BOTTOM_LINE, TOP_VERTICAL_LINES, BOTTOM_VERTICAL_LINES, LEFT_VERTICAL_LINES, RIGHT_VERTICAL_LINES, TOP_BOTTOM_LINES, TOP_MIDDLE_LINES, MIDDLE_BOTTOM_LINES, ALL_SEGMENTS]

#Variables and an array to hold pin values. Variables are assigned pin values with function  initPins_1Digit 
pins = []
digitPins = []
charactersToDisplay = []

def initPins_4Digit(a, b, c, d, e, f, g, dp):
	
 
	pA = machine.Pin(a, machine.Pin.OUT)
	pB = machine.Pin(b, machine.Pin.OUT)
	pC = machine.Pin(c, machine.Pin.OUT)
	pD = machine.Pin(d, machine.Pin.OUT)
	pE = machine.Pin(e, machine.Pin.OUT)
	pF = machine.Pin(f, machine.Pin.OUT)
	pG = machine.Pin(g, machine.Pin.OUT)
	pDP = machine.Pin(dp, machine.Pin.OUT)

	pins.append(pDP)
	pins.append(pG)
	pins.append(pF)
	pins.append(pE)
	pins.append(pD)
	pins.append(pC)
	pins.append(pB)
	pins.append(pA)

#Initializes and fills array of digit pins

def initDigitPins_4Digit(d1, d2, d3, d4):
	
	D1 = machine.Pin(d1, machine.Pin.OUT)
	D2 = machine.Pin(d2, machine.Pin.OUT)
	D3 = machine.Pin(d3, machine.Pin.OUT)
	D4 = machine.Pin(d4, machine.Pin.OUT)
	
	digitPins.append(D1)
	digitPins.append(D2)
	digitPins.append(D3)
	digitPins.append(D4)


#Clears Segment Display before writing a new output to it.	

def clearDisplay_4Digit():
	for i in range(8):
		pins[i].value((BLANK >> i ) & 1)

#Writes to display with a binary value. A change is made to the array of pin values, whether they are high or low.
#Bitwise operations go through the binary string right to left, if 1 appears, a pin is set high. If 0 appears, low.

def writeToDisplay_4Digit(first, second, third, fourth):

	charactersToDisplay.append(first)
	charactersToDisplay.append(second)
	charactersToDisplay.append(third)
	charactersToDisplay.append(fourth)


	for i in range(4):
		
		#Clear Segments			
	        clearDisplay_4Digit()
		
		#Set DigitPin On
		digitPins[i].value(0)		
		
		#Fill digit pin with segments
		for j in range(8):
			pins[j].value((charactersToDisplay[i] >> j) & 1)
			 

		time.sleep_ms(2)
				
		#Set DigitPin Off
		digitPins[i].value(1)

		

	


#function to test display, iterates through all possible display options for the 4 digit display

def testDisplay_4Digit():

	for i in numbers:
		time.sleep_ms(100)
		writeToDisplay_4Digit(i,i,i,i)
	for j in letters:
		time.sleep_ms(100)
		writeToDisplay_4Digit(j, j, j, j)	
	for k in special:
		time.sleep_ms(100)
		writeToDisplay_4Digit(k, k, k, k )

		
	
	
	
	
