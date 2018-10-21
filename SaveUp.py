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
	
def txn_detail_action(sender):
	sender.tableview.superview['tableview1'].hidden = True
	sender.tableview.superview['tableview1'].send_to_back()
	sender.tableview.superview['tableview2'].hidden = True
	sender.tableview.superview['tableview2'].send_to_back()
	sender.tableview.superview['textview1'].hidden = False
	sender.tableview.superview['textview1'].bring_to_front()
			
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
4u5IpwoSCLF/16
'''
import ui
import bz2
from base64 import b64decode
pyui = bz2.decompress(b64decode(data))
v = ui.load_view_str(pyui.decode('utf-8'))

# ------------------------

v.name = '$aveUp^'
v['imageview1'].image = ui.Image.named('SelectSite.png')
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


