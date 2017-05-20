#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- 
#
# main.py
# Copyright (C) 2017 Collin Norwood <cnorwood7641@stu.neisd.net>


import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class WelcomeWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Unnamed thingy")
		self.set_border_width(10)

		box = Gtk.Box(spacing=6)
		self.add(box)
		stepsbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		box.add(stepsbox)

		step1label = Gtk.Label("Step 1")
		stepsbox.add(step1label)
		step2label = Gtk.Label("Step 2")
		stepsbox.add(step2label)
		step3label = Gtk.Label("Step 3")
		stepsbox.add(step3label)
		step4label = Gtk.Label("Step 4")
		stepsbox.add(step4label)
		step5label = Gtk.Label("Step 5")
		stepsbox.add(step5label)

		mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		box.add(mainbox)

		welcomelabel = Gtk.Label("Welcome to this unnamed thingy. Hopefully this will let you install arch linux at some point. As you chose options and click next on each page it will basically make a script based on what options you selected.")
		mainbox.add(welcomelabel)
		testcheck = Gtk.CheckButton("Test")
		mainbox.add(testcheck)
		radio1 = Gtk.RadioButton("radio1")
		radio2 = Gtk.RadioButton(group=radio1, label="radio2")
		mainbox.pack_start(radio1, False, False, padding=5)
		mainbox.pack_start(radio2, False, False, padding=5)

		buttonbox = Gtk.Box(spacing=6)
		mainbox.pack_end(buttonbox, False, False, padding=0)

		button = Gtk.Button.new_with_label("Exit")
		button.connect("clicked", self.quitbutton)
		buttonbox.pack_start(button, False, False, padding=0)

		button = Gtk.Button.new_with_label("Next")
		button.connect("clicked", self.nextbutton, testcheck.get_active)
		buttonbox.pack_end(button, False, False, padding=0)

		button = Gtk.Button.new_with_label("Back")
		button.connect("clicked", self.backbutton)
		buttonbox.pack_end(button, False, False, padding=0)

	def nextbutton(self, button, checked):
		print(checked())
		f = open("out.sh", "a");
		f.write(str(checked) + "\n")
		win = SecondWindow()
		Gtk.Window.resize(win,800,500)
		win.connect("delete-event", Gtk.main_quit)
		win.show_all()
		Gtk.main()

	def backbutton(self, button, back):
 		print("back")
		
	def quitbutton(self, button):
		print("exit")
		Gtk.main_quit()

class SecondWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Unnamed thingy")
		self.set_border_width(10)

		box = Gtk.Box(spacing=6)
		self.add(box)
		stepsbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		box.add(stepsbox)

		step1label = Gtk.Label("Step 1")
		stepsbox.add(step1label)
		step2label = Gtk.Label("Step 2")
		stepsbox.add(step2label)
		step3label = Gtk.Label("Step 3")
		stepsbox.add(step3label)
		step4label = Gtk.Label("Step 4")
		stepsbox.add(step4label)
		step5label = Gtk.Label("Step 5")
		stepsbox.add(step5label)

		mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		box.add(mainbox)

		welcomelabel = Gtk.Label("Welcome to the second window.")
		mainbox.add(welcomelabel)

		buttonbox = Gtk.Box(spacing=6)
		mainbox.add(buttonbox)

		button = Gtk.Button.new_with_label("Exit")
		button.connect("clicked", self.quitbutton)
		buttonbox.pack_start(button, True, True, padding=0)

		button = Gtk.Button.new_with_label("Next")
		button.connect("clicked", self.nextbutton)
		buttonbox.pack_end(button, True, True, padding=0)

		button = Gtk.Button.new_with_label("Back")
		button.connect("clicked", self.backbutton)
		buttonbox.pack_end(button, True, True, padding=0)

	def nextbutton(self, button):
		print("next")

	def backbutton(self, button):
		print("back")

	def quitbutton(self, button):
		print("exit")
		Gtk.main_quit()

win = WelcomeWindow()
Gtk.Window.resize(win,800,500)
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
