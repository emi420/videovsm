#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' 
IPCam 

You may use any Piment project under the terms
of the GNU General Public License (GPL) Version 3.

(c) 2017 Emilio Mariscal (emi420 [at] gmail.com)

'''

import pexpect
import sys

class IPCam(object):

    def __init__(self, url, width, height):
        self.url = url
        self.width = width
        self.height = height
        

    def play(self):

        cmd = 'omxplayer --avdict "rtsp_transport:tcp" --win "0 0 ' + str(self.width) +  ' ' + str(self.height) + '" "' + self.url + '"'
        self.p = pexpect.spawn(cmd, timeout=None) 

        self.p.expect([pexpect.EOF, 'Have a nice day','Error'])
        print("Reconnecting ...")
        self.stop()
        self.play()

        return 1

    def stop(self):
        self.p.kill(0)
        return "Stopped."


if __name__ == '__main__':
    
    if len(sys.argv) > 0:
        url = sys.argv[1]
        width = 1950
        height = 1100
        if len(sys.argv) > 2:
            width = sys.argv[2]
            if len(sys.argv) > 3:
                height = sys.argv[3]

        ipcam = IPCam(url=url, width=width, height=height)
        ipcam.play()

    else:
        print("Usage: ipcam.py <channel> <width> <height>")


