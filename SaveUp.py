#import requests
#import pprint
#import time
import json

def weekly_total_action(sender):
	v['view1'].send_to_back()
#	v['view1'].hidden = True
	v['Transactions'].bring_to_front()
	v['Transactions'].hidden = False
	v['Transactions'].present('popover',hide_close_button=False)
	
def sweep_action(sender):

	v['view1'].send_to_back()
#	v['view1'].hidden = True
	v['Congradulations'].bring_to_front()
	v['Congradulations'].hidden = False
	v['Congradulations'].present('popover',hide_close_button=False)
	
def reset_view(sender):
	v['view1'].bring_to_front()
	v['view1'].hidden = False
	v['Transactions'].send_to_back()
	v['Transactions'].hidden = True
	v['Congradulations'].send_to_back()
	v['Congradulations'].hidden = True

def segmented_action(sender):
#	if sender.segments[sender.selected_index] == 'meetinggoalsegment':
	sender.selected_index = 0 #reset 
	v['view1']['saveuptosegment'].selected_index += 1

data = '''\
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
IMsyKegA==
'''
import ui
import bz2
from base64 import b64decode
pyui = bz2.decompress(b64decode(data))
v = ui.load_view_str(pyui.decode('utf-8'))

# ------------------------

v.name = '$aveUp^'
v['Transactions'].hidden = True
v['Congradulations'].hidden = True
v['Congradulations']['imageview1'].image = ui.Image.named('IMG_0417.PNG')
#v['Congradulations'].hidden = False
#v['Congradulations'].bring_to_front()

#v['meetinggoalsegment'].action = segmented_action
#v['button1'].action = segmented_action

#av = ui.load_view()
v.present('sheet')


