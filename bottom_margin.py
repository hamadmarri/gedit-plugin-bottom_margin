# Description: Set bottom margin (i.e. scroll past end)
# Authors: Hamad Al Marri <hamad.s.almarri@gmail.com>
# Copyright: Copyright (C) 2020 Hamad Al Marri
# Website: https://github.com/hamadmarri

from gi.repository import GObject, Gtk, Gedit

class BottomMargin(GObject.Object, Gedit.ViewActivatable):
	__gtype_name__ = "BottomMargin"
	view = GObject.property(type=Gedit.View)
	pixels = 800 # <<-- set this (default = 0)

	def __init__(self):
		GObject.Object.__init__(self)

	def do_activate(self):
		if self.view:
			self.view.set_bottom_margin(self.pixels)


	def do_deactivate(self):
		if self.view:
			self.view.set_bottom_margin(0)
