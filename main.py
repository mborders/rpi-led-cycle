from time import sleep
from led_thread import LedThread
import config
import pins

pins.init()
print('Starting loop')

if config.RUNNING:
    LedThread().start()

while True:
  if pins.red_button_pressed():
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

  pins.check_blue_led()
  pins.check_yellow_led()
  pins.check_green_led()
  sleep(0.1)