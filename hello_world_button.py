# Created by: Jacob Liberty 
# Created on: September 14 2017
# Created for: ICS3U
# This program is a button on a gui that will say Hello, World!

import ui

def hello_world_touch_up_inside(sender):
	#print ('Hello, World!')
	view['hello_world_label'].text = ("Hello,World!")

view = ui.load_view()
view.present('sheet')
