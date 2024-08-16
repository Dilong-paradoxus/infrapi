# infrapi
Miscellaneous code for Raspberry Pi IR camera, including a camera app and case design (eventually)
(More info and pics at my website maybe)

# Theory
The CMOS camera sensors used in most modern digital cameras are sensitive to light wavelengths beyond the visible spectrum, including near infrared. Typically, they have a filter to remove this light but the Raspberry Pi IR camera comes without this. In all other respects it is identical to the regular Pi Camera, so code made for that can be used for the IR version.

Healthy plants typically reflect strongly in near infrared, so vegetation is often the most striking feature of infrared images. Near infrared should not be confused with far/thermal infrared used in heat vision cameras. That requires exotic (and expensive) sensor and lens materials and is subject to export controls (at least in the US). 

# Hardware
Required:
* Raspberry Pi (software tested on Pi 2B)
* Pi NoIR camera V2
* Some kind of touchscreen (Software tested with Adafruit 3.5" 320x480 screen)

Recommended:
* WiFi Adapter for communication if your pi doesn't have one (good luck lmao)

# Skills Recommended:
* Linux Command Line
* Plugging things into other things
* Patience 

# Install Instructions
1. Install Raspberry Pi OS https://www.raspberrypi.com/software/
2. Plug in Pi Camera 
3. Download picamera_functions.py to a convenient location
4. Run picamera_functions.py (you can use an IDE like Thonny or run it from the command line)
5. Take pictures!
