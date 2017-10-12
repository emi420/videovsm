#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
from xml.dom import minidom
from time import sleep
import random
import math
from PIL import Image, ImageTk

master = Tk()
master.geometry('1950x1100')

canvas = Canvas(master, width=1950, height=1100, bd=0, highlightthickness=0, relief='ridge')
canvas.config(background="#000")
canvas.pack()

text1 = None
text2 = None
text3 = None

label1 = canvas.create_text(1500, 80, font=("Purisa", 20, "bold"), text="BPM", fill="#93C72A")
label2 = canvas.create_text(1500, 430, font=("Purisa", 20, "bold"), text="TMP", fill="#FBD234")
label3 = canvas.create_text(1500, 780, font=("Purisa", 20, "bold"), text="SAT", fill="#6ECDE3")

image = Image.open('heart.png')
image = image.resize((64, 64))
imageFinal = ImageTk.PhotoImage(image)

pic_heart = Label(master, image = imageFinal, borderwidth=0, bg="#000")
pic_heart.pack()
pic_heart.place(x = 1750, y = 130)

while 1:
	master.update()

	xmldoc = minidom.parse('response.xml')
	itemlist = xmldoc.getElementsByTagName("OBX")
	vsmdata = {}

	for item in itemlist:
		itemdata =  item.getElementsByTagName("OBX.6")[0].childNodes[0].data
		if itemdata == "bpm":
			vsmdata["bpm"] = item.getElementsByTagName("OBX.5")[0].childNodes[0].data	

		elif itemdata == "C":
			vsmdata["c"] = item.getElementsByTagName("OBX.5")[0].childNodes[0].data

		elif itemdata == "mmHg":
			vsmdata["mmhg"] = item.getElementsByTagName("OBX.5")[0].childNodes[0].data

	if text1 is not None:
		canvas.delete(text1)
		canvas.delete(text2)
		canvas.delete(text3)

	# Random data for testing
	#vsmdata["bpm"] = int(math.floor(random.random() * 100))
	#vsmdata["c"] = int(math.floor(random.random() * 100))
	#vsmdata["mmhg"] = int(math.floor(random.random() * 100))

	if vsmdata["bpm"] < 10:
		strbpm = "0" + str(vsmdata["bpm"])
	else:
		strbpm = str(vsmdata["bpm"])
	if vsmdata["c"] < 10:
		strc = "0" + str(vsmdata["c"])
	else:
		strc = str(vsmdata["c"])
	if vsmdata["mmhg"] < 10:
		strmmhg = "0" + str(vsmdata["mmhg"])
	else:
		strmmhg = str(vsmdata["mmhg"])

	text1 = canvas.create_text(1600, 180, font=("Purisa", 100, "bold"), text=strbpm, fill="#93C72A")
	text2 = canvas.create_text(1600, 530, font=("Purisa", 100, "bold"), text=strc, fill="#FBD234")
	text3 = canvas.create_text(1600, 880, font=("Purisa", 100, "bold"), text=strmmhg, fill="#6ECDE3")

	canvas.pack()

	sleep(1)


