from time import sleep
import config
import pins

pins.init()
print('Starting loop')

while True:
  if pins.red_button_pressed():
    sleep(0.1)
    pins.check_led_cycle()

  pins.check_blue_led()
  pins.check_yellow_led()
  pins.check_green_led()
  sleep(0.1)