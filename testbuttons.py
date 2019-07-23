import RPi.GPIO as GPIO

def call(channel):
    print('pushed')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(10, GPIO.RISING, callback=call)

message = input("Press enter to quit\n\n")

GPIO.cleanup()

# Borrowed code used to just check that my buttons work
# Got it from https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/
