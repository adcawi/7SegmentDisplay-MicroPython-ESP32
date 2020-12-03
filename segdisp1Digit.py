import machine
import time


#Below are variables used to write to the 1 digit display. A binary string represents which of the 8 segments/pins is high or low, depending on what letter, number, or special visual you want.

#UPPERCASE LETTERS 

LETTER_A = int('0b11101110', 2)
LETTER_C = int('0b10011100', 2)
LETTER_E = int('0b10011110', 2)
LETTER_F = int('0b10001110', 2)
LETTER_H = int('0b01101110', 2)
LETTER_L = int('0b00011100', 2)
LETTER_I = int('0b00001100', 2)
LETTER_O = int('0b11111100', 2)
LETTER_P = int('0b11001110', 2)
LETTER_S = int('0b10110110', 2)
LETTER_G = int('0b10111110', 2)
LETTER_J = int('0b01111000', 2)
LETTER_U = int('0b01111100', 2)


#LOWERCASE LETTERS


LETTER_b = int('0b00111110', 2)
LETTER_c = int('0b00011010', 2)
LETTER_d = int('0b01111010', 2)
LETTER_h = int('0b00101110', 2)
LETTER_n = int('0b00101010', 2)
LETTER_o = int('0b00111010', 2)
LETTER_r = int('0b00001010', 2)
LETTER_u = int('0b00111000', 2)
LETTER_y = int('0b01110110', 2)

#Array for testing purposes

letters = [LETTER_A, LETTER_C, LETTER_E, LETTER_F, LETTER_H, LETTER_L, LETTER_I, LETTER_O, LETTER_P, LETTER_S, LETTER_G, LETTER_J, LETTER_U, LETTER_b, LETTER_c, LETTER_d, LETTER_h, LETTER_n, LETTER_o, LETTER_r, LETTER_u, LETTER_y]

#NUMBERS

NUM_0 = int('0b11111100', 2)
NUM_1 = int('0b01100000', 2)
NUM_2 = int('0b11011010', 2)
NUM_3 = int('0b11110010', 2)
NUM_4 = int('0b01100110', 2)
NUM_5 = int('0b10110110', 2)
NUM_6 = int('0b10111110', 2)
NUM_7 = int('0b11100000', 2)
NUM_8 = int('0b11111110', 2)
NUM_9 = int('0b11110110', 2)


#Array for testing purposes

numbers = [ NUM_0, NUM_1, NUM_2, NUM_3, NUM_4, NUM_5, NUM_6, NUM_7, NUM_8, NUM_9]

#SPECIAL

BLANK = int('0b00000000', 2)
DP = int('0b00000001', 2)
VERTICAL_LINES = int('0b01101100', 2)
HORIZONTAL_LINES = int('0b10010010', 2)
TOP_LINE = int('0b10000000', 2)
MIDDLE_LINE = int('0b00000010', 2)
BOTTOM_LINE = int('0b00010000', 2)
TOP_VERTICAL_LINES = int('0b01000100', 2)
BOTTOM_VERTICAL_LINES = int('0b00101000', 2)
LEFT_VERTICAL_LINES = int('0b00001100', 2)
RIGHT_VERTICAL_LINES = int('0b01100000', 2)
TOP_BOTTOM_LINES = int('0b10010000', 2)
TOP_MIDDLE_LINES = int('0b10000010', 2)
MIDDLE_BOTTOM_LINES = int('0b00010010', 2)
ALL_SEGMENTS = int('0b11111111', 2)

#Array for testing purposes

special = [BLANK, DP, VERTICAL_LINES, HORIZONTAL_LINES, TOP_LINE, MIDDLE_LINE, BOTTOM_LINE, TOP_VERTICAL_LINES, BOTTOM_VERTICAL_LINES, LEFT_VERTICAL_LINES, RIGHT_VERTICAL_LINES, TOP_BOTTOM_LINES, TOP_MIDDLE_LINES, MIDDLE_BOTTOM_LINES, ALL_SEGMENTS]

#Variables and an array to hold pin values. Variables are assigned pin values with function 'initPins_1Digit'
pins = []

def initPins_1Digit(a, b, c, d, e, f, g, dp):
	
 
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


	
	  
#Clears Segment Display before writing a new output to it.	

def clearDisplay_1Digit():
	for i in range(8):
		pins[i].value(int(bin(BLANK >> i & 1)[2:]))

#Writes to display with a binary value. A change is made to the array of pin values, whether they are high or low.
#Bitwise operations go through the binary string right to left, if 1 appears, a pin is set high. If 0 appears, low.

def writeToDisplay_1Digit(toDisplay):

	clearDisplay_1Digit()
	
	for i in range(8):
		pins[i].value(int(bin(toDisplay >> i & 1)[2:]))
	
	

#function to test display, iterates through all possible display options for the 1 digit display

def testDisplay_1Digit():

	for i in numbers:
		time.sleep_ms(250)
		writeToDisplay_1Digit(i)
	for j in letters:
		time.sleep_ms(250)
		writeToDisplay_1Digit(j)	
	for k in special:
		time.sleep_ms(250)
		writeToDisplay_1Digit(k)

		
	
	
	
	
