import RPi.GPIO as GPIO
from .DHT11_Python import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=14)

def moist():
	result = instance.read()
	if result.is_valid():
	    print("Last valid input: " + str(datetime.datetime.now()))

	    #print("Temperature: %-3.1f C" % result.temperature)
	    return str("Humidity: %-3.1f %%" % result.humidity)
        

try:
    moist()


except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()
