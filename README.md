  #7SegmentDisplay-MicroPython-ESP32

  Module to use with an ESP32 with Micropython firmware to drive a 7-Segment Display. 
  Aim was to have simple methods in the main loop of a esp32 micropython microcontroller to drive a 7seg display. 

  In the finished form of the repo it should have four seperate modules, 
  1. 1Digit 7-Segment Display
  2. 4Digit 7-Segment 
  3. 1Digit 7-Segment Display with Shift Register
  4. 4Digit 7-Segment Display with Shift Register

  In function names a suffix is usually added in the form of _1Digit or _4Digit, which I found necessary 
  in order to be able to use both a 4 digit and 1 digit display in one project. 
 
 
  Micropython works with a boot.py file, and a main.py file.  

  Main.py contains an example how to use the display in 3 steps.  

  1. importing library 
  2. Initializing pins  
  3. Writing to the display  


  Boot.py was set up minimally, with os.debug turned off for ampy, and webrepl started. 

  segdisp1Digit.py is the name of the module that has all the functions to use in main.py. 

  It contains several constants you use to specify which to display, 

  Ex. segdisp1Digit.writeToDisplay_1Digit(segdisp1Digit.NUM_5) will display the number 5.

  CONSTANTS

 
  UPPERCASE LETTERS

  LETTER_A 
  LETTER_C  
  LETTER_E 
  LETTER_F  
  LETTER_H  
  LETTER_L  
  LETTER_I  
  LETTER_O  
  LETTER_P  
  LETTER_S  
  LETTER_G  
  LETTER_J  
  LETTER_U

  LOWERCASE LETTERS

  LETTER_b    
  LETTER_c    
  LETTER_d    
  LETTER_h    
  LETTER_n    
  LETTER_o    
  LETTER_r    
  LETTER_u    
  LETTER_y


  NUMBERS

  NUM_0     
  NUM_1     
  NUM_2     
  NUM_3     
  NUM_4     
  NUM_5     
  NUM_6     
  NUM_7     
  NUM_8     
  NUM_9 


  SPECIAL

  BLANK 
  DP 
  VERTICAL_LINES
  HORIZONTAL_LINES 
  TOP_LINE 
  MIDDLE_LINE 
  BOTTOM_LINE 
  TOP_VERTICAL_LINES 
  BOTTOM_VERTICAL_LINES 
  LEFT_VERTICAL_LINES 
  RIGHT_VERTICAL_LINES 
  TOP_BOTTOM_LINES 
  TOP_MIDDLE_LINES 
  MIDDLE_BOTTOM_LINES 
  ALL_SEGMENTS 




