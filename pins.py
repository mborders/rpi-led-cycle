from time import sleep
import RPi.GPIO as GPIO
import config

def off():
    for p in config.PINS:
        GPIO.output(p, GPIO.LOW)
    sleep(0.5)

def setOutput(pin, level, sleepSec):
    GPIO.output(pin, level)
    sleep(sleepSec)

def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)

    for p in config.PINS:
        GPIO.setup(p, GPIO.OUT, initial=GPIO.LOW)