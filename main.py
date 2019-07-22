from time import sleep
from heartbeat_thread import HeartbeatThread
import pins
import config

pins.init()

hb = HeartbeatThread(config.HEARTBEAT_LED, config.HEARTBEAT_TIME)
hb.start()

print('Starting loop')
while True:
  pins.check_led_cycle()
  pins.check_blue_led()
  pins.check_yellow_led()
  pins.check_green_led()
  sleep(0.1)