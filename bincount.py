#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: <Richard Masson>
Student Number: <MSSRIC004>
Prac: <1>
Date: <23/06/19>
"""
# define pin numbers for later
led1 = 11
led2 = 16
led3 = 15
but1 = 12
but2 = 7

# counter tracker
counter = 0 #track the digital count that the LEDs must display

# import Relevant Librares
import RPi.GPIO as GPIO
import time
import itertools
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led1, GPIO.OUT) #output for the LEDs
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup((but1,but2), GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #input for the buttons

def press_1(channel):
    #print('Decrement')
    global counter
    if (counter == 0): #rollunder protection
        counter = 7
    else:
        counter -= 1

def press_2(channel):
    #print('Increment')
    global counter
    if (counter == 7): #rollover protection
        counter = 0
    else:
        counter += 1

def press_toggle(channel):
    GPIO.output(led1, not GPIO.input(led1)) #interrupt handler

# interrupt stuff
GPIO.add_event_detect(but1, GPIO.RISING, callback=press_1, bouncetime=250) #dec
GPIO.add_event_detect(but2, GPIO.RISING, callback=press_2, bouncetime=250) #inc

# binary table creation
table = itertools.product('01', repeat=3) #generate iterator with binary values
arr = []
for i in table:
    arr.append(i) #convery this to an array of binary lists
    # for easier element retrieval

# Logic that you write
def main():
    readout = arr[counter] #get the current binary value array
    in1 = int(readout[0]) #typecast the string in place 1 to int
    in2 = int(readout[1]) #same here
    in3 = int(readout[2]) #same here
    GPIO.output(led1,in1) #LED state should match the int from respective element
    GPIO.output(led2,in2)
    GPIO.output(led3,in3)
    
# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except:
        GPIO.cleanup()
        print("Some other error occurred")


