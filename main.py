from heartbeat_thread import HeartbeatThread
from pin_thread import PinThread
import pins
import config

# Setup GPIO
pins.init()

# Heartbeat to indicate application is running
ht = HeartbeatThread(config.HEARTBEAT_LED, config.HEARTBEAT_TIME)
ht.start()

# Pin input/output checks
pt = PinThread(config.LED_CYCLE_TIME)
pt.start()
