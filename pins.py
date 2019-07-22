from time import sleep
from led_thread import LedThread
import RPi.GPIO as GPIO
import config

def off():
    for p in config.PINS:
        GPIO.output(p, GPIO.LOW)

def setOutput(pin, level, sleepSec):
    GPIO.output(pin, level)
    sleep(sleepSec)

def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(config.RED_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(config.BLUE_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(config.YELLOW_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(config.HEARTBEAT_LED, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(config.BLUE_LED, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(config.YELLOW_LED, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(config.GREEN_LED, GPIO.OUT, initial=GPIO.LOW)

    for p in config.PINS:
        GPIO.setup(p, GPIO.OUT, initial=GPIO.LOW)

    if config.RUNNING:
        LedThread().start()

def red_button_pressed():
    return GPIO.input(config.RED_BUTTON)

def blue_button_pressed():
    return GPIO.input(config.BLUE_BUTTON)

def yellow_button_pressed():
    return GPIO.input(config.YELLOW_BUTTON)

def check_led_cycle():
    if red_button_pressed() and not config.RED_BUTTON_DOWN:
        config.RED_BUTTON_DOWN = True
        if config.RUNNING:
            config.LOCK.acquire()
            config.RUNNING = False
            config.LOCK.release()
            off()
        else:
            config.LOCK.acquire()
            config.RUNNING = True
            config.LOCK.release()
            LedThread().start()
    elif not red_button_pressed():
        config.RED_BUTTON_DOWN = False

def check_blue_led():
    if blue_button_pressed() and not yellow_button_pressed():
        GPIO.output(config.BLUE_LED, GPIO.HIGH)
    else:
        GPIO.output(config.BLUE_LED, GPIO.LOW)

def check_yellow_led():
    if yellow_button_pressed() and not blue_button_pressed():
        GPIO.output(config.YELLOW_LED, GPIO.HIGH)
    else:
        GPIO.output(config.YELLOW_LED, GPIO.LOW)

def check_green_led():
    if blue_button_pressed() and yellow_button_pressed():
        GPIO.output(config.GREEN_LED, GPIO.HIGH)
    else:
        GPIO.output(config.GREEN_LED, GPIO.LOW)