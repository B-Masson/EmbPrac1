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

# import Relevant Librares
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

# Logic that you write
def main():
    GPIO.output((led1, led2, led3), GPIO.HIGH)


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
        print("Some other error occurred")
