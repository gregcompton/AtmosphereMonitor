# AtmosphereMonitor
Code for devices XBee + BME280
By default, XBee device sends payload to a coordinator (64-bit Address {0X00}). This 

## Hardware

- Atmospheric Sensor - BME280 - https://www.sparkfun.com/products/13676
- 2 Radios (pick between these options. You can mix and match.): 
  - XBee 3 (through hole) - https://www.sparkfun.com/products/15130 OR
  - XBee 3 Pro (through hole) - https://www.sparkfun.com/products/15131
- Sparkfun XBee Explorer - https://www.sparkfun.com/products/11812
  - An easy option for loading micropython code onto the radio and powering the radio and sensor
  - Alternatively, any FTDI programmer would work too (if you don't know how to connect the radio to an FTDI programmer, get the Explorer)
- Antenna (2.4GHz) - https://www.sparkfun.com/products/145
- USB Mini-B Cable - https://www.sparkfun.com/products/11301  - There is nothing special about this cable. If you have one already, then use it.
- Battery (optional)
    - Coin cell battery - Any 3V battery will work. 
    - If the Exploer is used, then a higher voltage (up to 5V) battery could be used. 
    - Note: If using the Explorer's 5V input, the voltage regulator will cause the setup to draw significantly more current in sleep mode (5V sleep = .370 mA vs 3V sleep = .015 mA). 

## Software 
- XCTU (if you don't know what this is, ##STOP## and do some remedial learning about XBee.)
- Pycharm XBee MicroPython plugin (optional)

## Resources
- Digi MicroPython Programming Guide: https://www.digi.com/resources/documentation/digidocs/PDFs/90002219.pdf  - Pycharm plugin info begins on page 32
- ToDo: Add link to youtube tutorial video

# Instructions
Before you begin, verify that XBee radio can be discovered in XCTU. If not, fundamental troubleshooting is required, which is beyond the scope of this document.
1. Assemble the endpoint sensor hardware
2. Configure XBee radio settings (XCTU)
2. Format XBee radio file system
3. Load code into XBee radio file system (XCTU File System Manager or Pycharm plugin)
4. Reset XBee radio

### Assemble the endpoint sensor hardware
ToDo: create fritz and add it here

This is a very standard/simple I2C implementation. 
| XBEE | BME280  |
|---|---|
| DI01  | SCL  |
|  DI11 | SDA  |
| 3.3V  | 3.3V  |
| GND  | GND  |


### Configure XBee raio settings using XCTU
**Endpoint Sensor Radio**
It is conceivable to set all of these programmatically at run time, in main.py, via AT commands. If you are going to try this, then you will simply use the default BD setting of 9600 to connect to the XBee radio file system.
- CE=0
- AP=2
- PS=1
- SM=6
- NI=Endpoint (this is optional, but I find it easier to name the radios when I'm working with many of them)
- BD=9600 (NOTE: you might try increasing this up to a max of 115200 if you have difficulties working with the file system. **DO NOT** go higher than this or things become unstable)

**Coordinator**
- CE=1
- AP=2
- NI=Coordinator (this is optional, but I find it easier to name the radios when I'm working with many of them)


### Format XBee radio file system
Using XCTU
1. Plug XBee radion into your computer
2. Open XCTU
3. Tools->File System Manager
4. Click Configure
5. Select XBee radio's serial port
6. Set Baud Rate to whatever you configured previously (default=9600) Leave everything else as the default (8, None, 1, None)
7. Click OK
8. Click Open (if the connection doesn't open, check that your baud rate settings)
9. Click Format. You will be prompted with "Are you sure you want to format the XBee file system?" Click Yes. *NOTE: If this is the first time the file system has been accessed, you may be prompted to format the file systme when the connection is opened. If so, then click OK.*

PyCharm *might* prompt you to format the file system when you connect to a radio. If so, that's fine.

### Load code into XBee radio file system
Using XCTU
1. On the "Remote path" side of the window, you should see "Remote path: /flash", a folder called "lib", and nothing else. This indicates that the file system was formatted properly. If this is not the case, go ahead and click the "Format" icon to re-format the file system.
2. On the "Local path" side of the window, navigate to the "AtmosphereMonitor" folder on your computer.
3. Click and drag BME280.py and main.py to the remote window. After uploading, the files should appear below the lib folder.

**Once the XBee is reset, you have 5 seconds to interupt the code and enter REPL. The best way to do this is to open the PORT then spam ctrl-c.**
