#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- 
#
# main.py
# Copyright (C) 2017 Collin Norwood <cnorwood7641@stu.neisd.net>


import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
from subprocess import call
import os
os.system("rm out.sh")
os.system("echo 'echo installing' > out.sh")
class installer(gtk.Window):

	def __init__(self):
		gtk.Window.__init__(self, title="Arch installer")
		self.set_border_width(10)
		box = gtk.Box(orientation=gtk.Orientation.VERTICAL)
		self.add(box)
		global mainbook
		mainbook = gtk.Notebook()
		box.pack_start(mainbook, True, True, padding=0)
		
		
		buttonbox = gtk.Box()
		box.pack_end(buttonbox, False, False, padding=5)
		
		button = gtk.Button.new_with_label("Exit")
		button.connect("clicked", self.quitbutton)
		buttonbox.pack_start(button, False, False, padding=5)

		button = gtk.Button.new_with_label("Next")
		button.connect("clicked", self.nextbutton)
		buttonbox.pack_end(button, False, False, padding=5)

		button = gtk.Button.new_with_label("Back")
		button.connect("clicked", self.backbutton)
		buttonbox.pack_end(button, False, False, padding=5)



		#Page 1
		softwarepage = gtk.Box(orientation=gtk.Orientation.VERTICAL, spacing=6)
		welcomelabel = gtk.Label("Chose some packages:")
		softwarepage.add(welcomelabel)
		global packages
		packages = [];

		global firefox
		firefox = gtk.CheckButton("firefox")
		softwarepage.add(firefox)
		packages.append(firefox)
		
		global gedit
		gedit = gtk.CheckButton("gedit")
		softwarepage.add(gedit)
		packages.append(gedit)
		
		global steam
		steam = gtk.CheckButton("steam")
		softwarepage.add(steam)
		packages.append(steam)
		
		global kdenlive
		kdenlive = gtk.CheckButton("kdenlive")
		softwarepage.add(kdenlive)
		packages.append(kdenlive)


		#Page 2
		displaypage = gtk.Box(orientation=gtk.Orientation.VERTICAL, spacing=6)
		welcomelabel = gtk.Label("Chose a display manager:")
		displaypage.add(welcomelabel)
				
		global wayland
		wayland = gtk.RadioButton("wayland")
		displaypage.add(wayland)
		packages.append(wayland)
		
		global x11
		x11 = gtk.RadioButton(group=wayland, label="x11")
		displaypage.add(x11)
		packages.append(x11)


		#Page 3
		partitionpage = gtk.Box(orientation=gtk.Orientation.VERTICAL, spacing=6)
		welcomelabel = gtk.Label("Chose your partition scheme")
		partitionpage.pack_start(welcomelabel, False, False, padding=5)
		partbox = gtk.Box()
		partitionpage.pack_end(partbox, True, True, padding=5)
		drivebox = gtk.Box(orientation=gtk.Orientation.VERTICAL, spacing=6)
		schemebox = gtk.Box(orientation=gtk.Orientation.VERTICAL, spacing=6)
		partbox.add(drivebox)
		partbox.add(schemebox)
		
		global drive1
		drive1 = gtk.RadioButton("/dev/sda")
		drivebox.add(drive1)
		
		global drive2
		drive2 = gtk.RadioButton(group=drive1, label="/dev/sdb")
		drivebox.add(drive2)
		
		global ext3
		ext3 = gtk.RadioButton("ext3")
		schemebox.add(ext3)
		
		global ext4
		ext4 = gtk.RadioButton(group=ext3, label="ext4")
		schemebox.add(ext4)
		
		#Page 4
		finalpage = gtk.Box(orientation=gtk.Orientation.VERTICAL, spacing=6)
		welcomelabel = gtk.Label("I'm now going to attempt to generate an install script based on the options you selected.\nYou Should review it very carefully. It will almost certainly destroy your machine otherwise.")
		finalpage.add(welcomelabel)
		gobutton = gtk.Button("GO!")
		gobutton.connect("clicked", self.gobutton)
		finalpage.pack_end(gobutton, False, False, padding=5)


		#Tabs
		tab1label = gtk.Label("Software")
		tab2label = gtk.Label("Display Manager")
		tab3label = gtk.Label("Disks")
		tab4label = gtk.Label("Finish")
		mainbook.append_page(softwarepage, tab1label)
		mainbook.append_page(displaypage, tab2label)
		mainbook.append_page(partitionpage, tab3label)
		mainbook.append_page(finalpage, tab4label)


	def nextbutton(self, button):
		mainbook.next_page()
		
	def gobutton(self, button):
		out = open("out.sh", "a");
		
		if ext3.get_active() == True:
			out.write("sudo mkfs.ext3 NO NO NO NO NO\n")
		if ext4.get_active() == True:
			out.write("sudo mkfs.ext4 NO NO NO NO NO\n")
		
		for package in packages:
			if package.get_active() == True:
				out.write("sudo dnf install " + package.get_label() + "\n")
			else:
				out.write("echo 'skipping " + package.get_label() + "'\n")
			
		out.write("echo 'Done!'")
			
		out.close()
		os.system("gnome-terminal -x sh -c 'bash out.sh; exec bash'")
		gtk.main_quit()

	def backbutton(self, button):
		mainbook.prev_page()
		
	def quitbutton(self, button):
		gtk.main_quit()

win = installer()
gtk.Window.resize(win,800,500)
win.connect("delete-event", gtk.main_quit)
win.show_all()
gtk.main()
