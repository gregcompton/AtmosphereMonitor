# AtmosphereMonitor
Code for devices XBee3 + BME280

By default, XBee device sends payload to a coordinator (64-bit Address {0X00}). 
- This can be changed to an explicit address in main.py by changing **TARGET_64BIT_ADDR = b'\x00\x00\x00\x00\x00\x00\x00\x00'** to the desired address (e.g. \x00\x13\xA2\x20....etc)

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
    - If the Explorer is used, then a higher voltage (up to 5V) battery could be used. 
    - Note: If using the Explorer's 5V input, the voltage regulator will cause the setup to draw significantly more current in sleep mode (5V sleep = .370 mA vs 3V sleep = .015 mA). 

## Software 
- XCTU (if you don't know what this is, **STOP** and do some remedial learning about XBee. Here are some videos I made on the subject: https://www.youtube.com/playlist?list=PL2MfcBwemUMscK12JcMxgHKZu0ZUGRizO)
- Pycharm XBee MicroPython plugin (optional. It's use is not covered in depth in these instructions)

*ToDo: Create XBee Micropython PyCharm Plugin tutorial*

## Resources
- PyCharm XBee MicroPython plugin: https://plugins.jetbrains.com/plugin/12445-xbee-micropython
- Digi MicroPython Programming Guide: https://www.digi.com/resources/documentation/digidocs/PDFs/90002219.pdf  - Pycharm plugin info begins on page 32
- Basic XBee XCTU tutorials: https://www.youtube.com/playlist?list=PL2MfcBwemUMscK12JcMxgHKZu0ZUGRizO

*ToDo: Create tutorial video for this project*

# Instructions
Before you begin, verify that the XBee radios can be discovered in XCTU. If not, fundamental troubleshooting is required, which is beyond the scope of this document. If you don't know how to do this, check out my tutorial here: https://youtu.be/AemzSO5EDy0
1. Assemble the endpoint sensor hardware
2. Configure XBee radio settings (XCTU)
2. Format XBee radio file system
3. Load code into XBee radio file system (XCTU File System Manager or Pycharm plugin)
4. Reset XBee radio and monitor Coordinator's console

### Assemble the endpoint sensor hardware
This is a very standard/simple I2C implementation. 
| XBEE | BME280  |
|---|---|
| DI01  | SCL  |
|  DI11 | SDA  |
| 3.3V  | 3.3V  |
| GND  | GND  |

If you want to run this on battery power, I'll leave it to you to figure out how to splice in 3V power from the battery

*ToDo: create fritz and add it here*

### Configure XBee raio settings using XCTU
If you need a refresher on configuring XBee radios and using API Mode, check out my tutorial here: https://youtu.be/AemzSO5EDy0

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
- NJ=FF (FF keeps the join window open forever. This is useful for testing. However, it should be changed to FE (or lower) for field deployment.
- NI=Coordinator (this is optional, but I find it easier to name the radios when I'm working with many of them)

Finally, test that Endpoint has joined Coordinator's PAN by sending a Hello World message. 


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

PyCharm *might* prompt you to format the file system when you connect to a radio. If so, that's fine, go for it.

### Load code into XBee radio file system
Using XCTU
1. On the "Remote path" side of the window, you should see "Remote path: /flash", a folder called "lib", and nothing else. This indicates that the file system was formatted properly. If this is not the case, go ahead and click the "Format" icon to re-format the file system.
2. On the "Local path" side of the window, navigate to the "AtmosphereMonitor" folder on your computer.
3. Click and drag BME280.py and main.py to the remote window. After uploading, the files should appear below the lib folder.

Using Pycharm with plugin
1. Open AtmosphereMonitor project in PyCharm
2. Set correct COM port for the Endpoint Sensor
3. Set the Project to AtmosphereMonitor folder
3. Click Build (hammer)
4. Click Run (arrow)
5. main.mpy and BME270.mpy will be flashed to radio
6. Endpoint Sensor radio will soft reboot

*ToDo: Create tutorial on how to load a file system OTA. Useful/necessary for implementation using SMT versionsof XBee3

### Reset XBee radio and monitor Coordinator's console
In XCTU, select Coordinator, then click Console.
You should see packets being received from Endpoint Sensor (default sample rate is 60 seconds)

While Endpoint Sensor is connected via usb to your computer, you can use MicroPython Terminal to monitor it.
1. In XCTU, click Tools->Micropython Terminal
2. Click Configure
3. Select correct COM port for Endpoint Sensor
4. Select correct Baud Rate for Endpoint Sensor
5. Click OK
6. Click Open

You should now see the payload in the terminal. 

NOTE: serial communications are closed while Endpoint is sleeping. You will need to spam ctrl-c in order to stop the program and enter REPL mode. The ctrl-c keyboard interrupt will only be detected when the radio wakes up. So, if you have changed sampleRate to a long sleep time (or you just don't want to wait 60 seconds), you can hard reset the device by pressing the RESET button on the XBee Explorer. **Once the XBee is reset, you have 5 seconds to interupt the code. The best way to do this is to open make sure Micropython Terminal is open to Endpoint Sensor then press the RESET button and spam ctrl-c.**
