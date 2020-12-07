import machine
import time

#############################################################################

#For the ESP-32, to take advantage of the shift register and output to the segment display, we will be using SPI to output bytes to the shift register. The two hardware options for the ESP32 are vspi and hspi, so initialize your pins in the functions below according to the documentation of the ESP32. 

# 6 Pins in total are needed for the shift register. 3 for SPI, 3 GPIO Pins, 4 more pins are needed for digits

# Ex. VSPI
# ~~~~~~~~
# SCK = PIN 18 (goes to SH/Clock/SerClock of Segment Shifter)
# MOSI = PIN 23 (goes to DS/SER/Data of Segment Shifter)
# MISO = PIN 19 (does not go to segment shifter)


# Create SPI object 
# vspi = SPI(2, baudrate=80000000, polarity=1, phase=0, bits=8, firstbit =0, sck= Pin(18), mosi=Pin(23), miso=Pin(19))


# 7  GPIO Pins 

# GPIO  = PIN 14 (goes to Latch/ST of Segment Shifter) 
# GPIO  = PIN 12 (goes to OE/Output Enable of Segment Shifter)
# GPIO = PIN 13 ( Goes to Master Reset/ Clear of Segment Shifter) 
# GPIO  = PIN 33 (goes to d1 of 4 digit display)
# GPIO = PIN  25 (goes to d2 of 4 digit display)
# GPIO = PIN 26  (goes to d3 of 4 digit display)
# GPIO = PIN 27 (goes to d4 of 4 digit display)

# In order of (SPI Object, rclk, oe, clr)
# segDisp1Digit.initPins_1Digit_595(vspi, 14, 12, 13)

##############################################################################

#Below are variables used to write to the 1 digit display. A binary string represents which of the 8 segments/pins is high or low, depending on what letter, number, or special visual you want.

#UPPERCASE LETTERS 

LETTER_A =   b'\x77'  
LETTER_C =   b'\x39'  
LETTER_E =   b'\x79' 
LETTER_F =   b'\x71'  
LETTER_H =   b'\x76'  
LETTER_L =   b'\x38'  
LETTER_I =   b'\x30'  
LETTER_O =   b'\x3F'  
LETTER_P =   b'\x73'  
LETTER_S =   b'\x6D'  
LETTER_G =   b'\x7D'  
LETTER_J =   b'\x1E'  
LETTER_U =   b'\x3E'  


#LOWERCASE LETTERS


LETTER_b =   b'\x7C' 
LETTER_c =   b'\x58'
LETTER_d =   b'\x5E'  
LETTER_h =   b'\x74'  
LETTER_n =   b'\x54'  
LETTER_o =   b'\x5C'  
LETTER_r =   b'\x50'  
LETTER_u =   b'\x1C'  
LETTER_y =   b'\x6E'  

#Array for testing purposes

letters = [LETTER_A, LETTER_C, LETTER_E, LETTER_F, LETTER_H, LETTER_L, LETTER_I, LETTER_O, LETTER_P, LETTER_S, LETTER_G, LETTER_J, LETTER_U, LETTER_b, LETTER_c, LETTER_d, LETTER_h, LETTER_n, LETTER_o, LETTER_r, LETTER_u, LETTER_y]

#NUMBERS

NUM_0 =   b'\x3F'  
NUM_1 =   b'\x06' 
NUM_2 =   b'\x5B'  
NUM_3 =   b'\x4F'  
NUM_4 =   b'\x66'  
NUM_5 =   b'\x6D'  
NUM_6 =   b'\x7D'  
NUM_7 =   b'\x07'  
NUM_8 =   b'\x7F'  
NUM_9 =   b'\x6F'  


#Array for testing purposes

numbers = [ NUM_0, NUM_1, NUM_2, NUM_3, NUM_4, NUM_5, NUM_6, NUM_7, NUM_8, NUM_9]

#SPECIAL

BLANK =   b'\x00'  
DP =   b'\x80'  
VERTICAL_LINES =   b'\x36'  
HORIZONTAL_LINES =   b'\x49'  
TOP_LINE =   b'\x01'  
MIDDLE_LINE =   b'\x40'  
BOTTOM_LINE =   b'\x08'  
TOP_VERTICAL_LINES =   b'\x22'  
BOTTOM_VERTICAL_LINES =   b'\x14'  
LEFT_VERTICAL_LINES =   b'\x30'  
RIGHT_VERTICAL_LINES =   b'\x06'  
TOP_BOTTOM_LINES =   b'\x09'  
TOP_MIDDLE_LINES =   b'\x41'  
MIDDLE_BOTTOM_LINES =   b'\x48'  
ALL_SEGMENTS =   b'\xFF'  

#Array for testing purposes

special = [BLANK, DP, VERTICAL_LINES, HORIZONTAL_LINES, TOP_LINE, MIDDLE_LINE, BOTTOM_LINE, TOP_VERTICAL_LINES, BOTTOM_VERTICAL_LINES, LEFT_VERTICAL_LINES, RIGHT_VERTICAL_LINES, TOP_BOTTOM_LINES, TOP_MIDDLE_LINES, MIDDLE_BOTTOM_LINES, ALL_SEGMENTS]


#Array to hold pin values. Variables are assigned pin values with function initPins_1Digit_595 
# SPI OBJECT, RCLK, OE, CLR
pins = [];	
digitPins =[]
charactersToDisplay = []

def initDigitPins_4Digit_595(d1, d2, d3, d4):
	D1 = machine.Pin(d1, machine.Pin.OUT)
	D2 = machine.Pin(d2, machine.Pin.OUT)
	D3 = machine.Pin(d3, machine.Pin.OUT)
	D4 = machine.Pin(d4, machine.Pin.OUT)

	digitPins.append(D1)
	digitPins.append(D2)
	digitPins.append(D3)
	digitPins.append(D4)

def initPins_4Digit_595(spiObject, rclk, oe, clr):
	
	spi = spiObject
	rclk = machine.Pin(rclk, machine.Pin.OUT)	
	oe   = machine.Pin(oe, machine.Pin.OUT)
	clr = machine.Pin(clr, machine.Pin.OUT)	
	
	pins.append(spi)
	pins.append(rclk)
	pins.append(oe)
	pins.append(clr)
	
	oe.value(0) #output enable
	clr.value(1) # dont reset shift reg
		  

def clearDisplay_4Digit_595():
	pins[3].value(0) #clear shift Reg
	pins[1].value(1) #latch data to output
	pins[1].value(0) 
	pins[3].value(1) 	

def writeToDisplay_4Digit_595(buf1, buf2, buf3, buf4):

	charactersToDisplay.append(buf1)
	charactersToDisplay.append(buf2)
	charactersToDisplay.append(buf3)
	charactersToDisplay.append(buf4)
	
	for i in range(4):
		#clear segments
		clearDisplay_4Digit_595()
		#Set DigitPin ON
		digitPins[i].value(0)
		#Fill Digit Pin with Segments

	
		pins[0].write(charactersToDisplay[i])
		pins[1].value(1) #latch data
		pins[1].value(0) 
      	        time.sleep_ms(5)	

		digitPins[i].value(1)

#function to test display, iterates through all possible display options for the 4 digit display

def testDisplay_4Digit_595():

	for i in numbers:
		time.sleep_ms(250)
		writeToDisplay_4Digit_595(i, i, i, i)
	for j in letters:
		time.sleep_ms(250)
		writeToDisplay_1Digit_595(j, j, j, j)	
	for k in special:
		time.sleep_ms(250)
		writeToDisplay_1Digit_595(k, k, k, k)

		
	
	
	
	
