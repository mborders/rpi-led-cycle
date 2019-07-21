import RPi.GPIO as GPIO
from time import sleep
import threading
import config
from led_thread import LedThread
import pins

pins.init()
print('Starting loop')

if config.RUNNING:
    LedThread().start()

while True:
  if GPIO.input(14):
    sleep(0.1)
    config.LOCK.acquire()
    isRunning = config.RUNNING
    config.LOCK.release()

    if isRunning:
      config.LOCK.acquire()
      pins.off()
      config.RUNNING = False
      config.LOCK.release()
    else:
      config.LOCK.acquire()
      config.RUNNING = True
      LedThread().start()
      config.LOCK.release()

  if GPIO.input(19) and not GPIO.input(6):
    GPIO.output(26, GPIO.HIGH)
  else:
    GPIO.output(26, GPIO.LOW)

  if GPIO.input(6) and not GPIO.input(19):
    GPIO.output(13, GPIO.HIGH)
  else:
    GPIO.output(13, GPIO.LOW)

  if GPIO.input(19) and GPIO.input(6):
    GPIO.output(5, GPIO.HIGH)
  else:
    GPIO.output(5, GPIO.LOW)

  sleep(0.1)