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
# define pins for later
led1 = 11
led2 = 16
led3 = 15
but1 = 12
but2 = 7

# counter tracker
counter = 0

# binary table
# list(itertools.product(*['1', 2))

# import Relevant Librares
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup((but1,but2), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def press_1(channel):
    print('Press 1')
    global counter
    if (counter == 7):
        counter = 0
    else:
        counter += 1

def press_2(channel):
    print('Press 2')
    global counter
    if (counter == 0):
        counter = 7
    else:
        counter -= 1

def press_toggle(channel):
    GPIO.output(led1, not GPIO.input(led1))

# interrupt stuff
GPIO.add_event_detect(but1, GPIO.RISING, callback=press_toggle, bouncetime=150)
GPIO.add_event_detect(but2, GPIO.RISING, callback=press_2, bouncetime=150)

# Logic that you write
def main():
    time.sleep(0.1)
    
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


