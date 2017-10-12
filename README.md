# Video+VSM

Display video stream and vital signs monitor's data on screen.

## Installation

### Raspberry Pi console-only

If you want to install this on a Raspberry Pi using a console-only installation, you'll need to install a minimal X11 first:

* sudo apt-get update
* sudo apt-get install xserver-xorg
* sudo apt-get install xinit
* sudo apt-get install xserver-xorg-video-fbdev

### 1. Clone this repository

* git clone https://github.com/emi420/videovsm.git

### 2. Install Requeriments

* cd videovsm && git clone https://github.com/emi420/ipcam.git
* pexpect (pip install pexpect)
* omxplayer (apt-get install omxplayer)
* sudo apt-get install python-tk
* sudo apt-get install libjpeg8-dev
* sudo pip install Pillow

### TIP: disable screensaver on X11

Edit ~/.xinitrc and add this:

```
xset s off
xset -dpms
xset s noblank
```

### 3. Configure & Run

* Check path in gui/start.sh
* Check path in video/start.sh
* Check paths in utils/rc.local and copy contents to /etc/rc.local
* Edit the stream's URL in video/start.sh
* Reboot

### Update VSM's data

Vital Signs Monitor's data is in HL7 format and loaded from gui/response.xml, you'll need to update that file in order to update data on screen.

## License

You may use any Mootor project under the terms of either the MIT License or the GNU General Public License (GPL) Version 3.

(c) 2017 Emilio Mariscal

Want to contribute? or use this software? fork the project, or write me to emi420 [at] gmail.com



