# AtmosphereMonitor
Code for endpoint devices XBee + BME280


Hardware (required): Atmospheric Sensor - BME280 - https://www.sparkfun.com/products/13676

Hardware (required): Radio (pick one): XBee 3 (through hole) - https://www.sparkfun.com/products/15130 OR
                    XBee 3 Pro (through hole) - https://www.sparkfun.com/products/15131
                    
Hardware (required): Antenna (2.4GHz) - https://www.sparkfun.com/products/145

Hardware (required): USB Mini-B Cable - https://www.sparkfun.com/products/11301  - There is nothing special about this cable. If you have one already, then use it.

Hardware (Required): Sparkfun XBee Explorer - https://www.sparkfun.com/products/11812
    - An easy option for loading micropython code onto the radio and powering the radio and sensor
    - Alternatively, any FTDI programmer would work too (if you don't know how to connect the radio to an FTDI programmer, get the Explorer)

Hardware (Optional): Battery
    - Coin cell battery - Any 3V battery will work. 
    - If the Exploer is used, then a higher voltage (up to 5V) battery could be used. 
      - Note: If using the Explorer's 5V input, the voltage regulator will cause the setup to draw significantly more current in sleep mode (5V sleep = .370 mA vs 3V sleep = .015 mA). 

Software (optional) - Pycharm XBee MicroPython plugin

Digi MicroPython Programming Guide: https://www.digi.com/resources/documentation/digidocs/PDFs/90002219.pdf  - Pycharm plugin info begins on page 32

ToDo: Add link to youtube tutorial video
