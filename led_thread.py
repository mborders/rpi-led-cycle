import threading
import RPi.GPIO as GPIO
import config
import pins


class LedThread(threading.Thread):
    def run(self):
        print('Starting lights')

        while True:
            for p in config.PINS:
                config.LOCK.acquire()
                if not config.RUNNING:
                    config.LOCK.release()
                    break
                config.LOCK.release()
                pins.setOutput(p, GPIO.HIGH, config.LED_CYCLE_TIME)
                pins.setOutput(p, GPIO.LOW, 0)

            config.LOCK.acquire()
            if not config.RUNNING:
                config.LOCK.release()
                break
            config.LOCK.release()

        print('Stopping lights')
