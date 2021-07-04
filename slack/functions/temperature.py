import RPi.GPIO as GPIO
from .DHT11_Python import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=14)

def temperature():
	result = instance.read()
	if result.is_valid():
	    print("Last valid input: " + str(datetime.datetime.now()))

	    return str("Temperature: %-3.1f C" % result.temperature)



try:
    temperature()


except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()

