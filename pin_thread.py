import threading
import pins
from time import sleep

class PinThread (threading.Thread):
    def __init__(self, time):
        threading.Thread.__init__(self)
        self.time = time

    def run(self):
        print('Starting pin loop')

        while True:
            pins.check_led_cycle()
            pins.check_blue_led()
            pins.check_yellow_led()
            pins.check_green_led()
            sleep(self.time)