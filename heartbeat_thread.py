import RPi.GPIO as GPIO
import threading
from time import sleep


class HeartbeatThread(threading.Thread):
    def __init__(self, pin, time):
        threading.Thread.__init__(self)
        self.on = False
        self.pin = pin
        self.time = time

    def run(self):
        print('Starting heartbeat')

        while True:
            if self.on:
                self.on = False
                GPIO.output(self.pin, GPIO.LOW)
            else:
                self.on = True
                GPIO.output(self.pin, GPIO.HIGH)

            sleep(self.time)
