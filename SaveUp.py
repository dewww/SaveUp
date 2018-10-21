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
	v['Congratulations'].bring_to_front()
	v['Congratulations'].hidden = False
	v['Congratulations'].present('popover',hide_close_button=False)
	
def reset_view(sender):
	v['view1'].bring_to_front()
	v['view1'].hidden = False
	v['Transactions'].send_to_back()
	v['Transactions'].hidden = True
	v['Congratulations'].send_to_back()
	v['Congratulations'].hidden = True

def segmented_action(sender):
#	if sender.segments[sender.selected_index] == 'meetinggoalsegment':
	sender.selected_index = 0 #reset 
	v['view1']['saveuptosegment'].selected_index += 1
	if v['view1']['saveuptosegment'].selected_index <= 0:
		v['view1']['imageview1'].hidden = True	
	else:
		v['view1']['imageview1'].hidden = True	
		v['view1']['imageview1'].image = ui.Image.named('IMG_042'+format(v['view1']['saveuptosegment'].selected_index)+'.PNG')
		v['view1']['imageview1'].hidden = False
	print('IMG_042'+format(v['view1']['saveuptosegment'].selected_index)+'.PNG')

		
data = '''\
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
'''
import ui
import bz2
from base64 import b64decode
pyui = bz2.decompress(b64decode(data))
v = ui.load_view_str(pyui.decode('utf-8'))

# ------------------------

v.name = '$aveUp^'
v['Transactions'].hidden = True
v['Congratulations'].hidden = True
v['Congratulations']['imageview1'].image = ui.Image.named('IMG_0417.PNG')
v['view1']['imageview1'].image = ui.Image.named('IMG_0420.PNG')
print('IMG_042'+format(v['view1']['saveuptosegment'].selected_index)+'.PNG')
#v['Congratulations'].hidden = False
#v['Congratulations'].bring_to_front()

#v['meetinggoalsegment'].action = segmented_action
#v['button1'].action = segmented_action

#av = ui.load_view()
v.present('sheet')


