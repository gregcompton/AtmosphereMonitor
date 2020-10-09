from machine import Pin, I2C
from time import sleep
import BME280
import xbee

TARGET_64BIT_ADDR = b'\x00\x00\x00\x00\x00\x00\x00\x00'
MESSAGE = ""
sleep_ms = 0
sampleRate = 60000 #milli-seconds
separator = " | "

# XBee hardware managed i2c
i2c1 = I2C(1, freq=400000)
i2c1.scan()

sleep(5)  # delay after boot to allow radio to join network

while True:
  bme = BME280.BME280(i2c=i2c1)

  temp = bme.temperature
  hum = bme.humidity

  voltage = str(xbee.atcmd("%V")/1000)

  MESSAGE = str(temp) + separator + str(hum) + separator + voltage + separator + str(sampleRate/1000)
  print(MESSAGE)

  try:
    xbee.transmit(TARGET_64BIT_ADDR, MESSAGE)
  except Exception as e:
      print("Transmit failure: %s" % str(e))

  sleep_ms = xbee.XBee().sleep_now(sampleRate, pin_wake=False)
  #sleep(2)