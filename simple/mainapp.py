import ui
from classified import Morpheus
from database import Patient, Act

def show_morpheus(sender):
	f=(0,0,350,650)
	tabs = ['All', 'Outpt', 'Inpt', 'Inactive']
	extra_tabs= ui.SegmentedControl()
	extra_tabs.segments = ['To See', 'Seen']
	extra_tabs.name = 'todaytab'
	items_toAdd = [{'title':'Patient', 'object':Patient()}, {'title':'Act', 'object':Act()}]
	Morpheus(Patient, items_toAdd, frame = f, tabs_contents = tabs, extra_data = extra_tabs)

	
v = ui.load_view()
#print(ui.get_screen_size())
v.present('sheet')
