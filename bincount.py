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

# import Relevant Librares
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(but1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def press_callback(channel):
    print('Success!')

# interrupt stuff
GPIO.add_event_detect(but1, GPIO.RISING, callback=press_callback, bouncetime=150)

# Logic that you write
def main():
    GPIO.output(led1, 1)
    time.sleep(1)
    GPIO.output(led1, 0)
    time.sleep(1)
    
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


