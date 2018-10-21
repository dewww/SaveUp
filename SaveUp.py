#import requests
#import pprint
#import time
import json

def weekly_total_action(sender):
	v['view1'].hidden = True
	v['view2'].bring_to_front()
	v['view2'].hidden = False

def sweep_action(sender):
	v['view3'].send_to_back()
#	v['view1'].hidden = True
	v['view3'].bring_to_front()
	v['view3'].hidden = False
	v['view3'].present('popover')
	
def reset_view(sender):
	v['view1'].bring_to_front()
	v['view1'].hidden = False
	v['view2'].send_to_back()
	v['view2'].hidden = True
	v['view3'].send_to_back()
	v['view3'].hidden = True

def segmented_action(sender):
#	if sender.segments[sender.selected_index] == 'meetinggoalsegment':
	sender.selected_index = 0 #reset 
	v['view1']['saveuptosegment'].selected_index += 1

data = '''\
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
MOGz/i7kinChIZGG/XYA==
'''
import ui
import bz2
from base64 import b64decode
pyui = bz2.decompress(b64decode(data))
v = ui.load_view_str(pyui.decode('utf-8'))

# ------------------------

v.name = '$aveUp^'
v['view2'].hidden = True
v['view3'].hidden = True
#v['view3'].hidden = False
#v['view3'].bring_to_front()

#v['meetinggoalsegment'].action = segmented_action
#v['button1'].action = segmented_action

#av = ui.load_view()
v.present('sheet')


