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
pjYH+/3P/4u5IpwoSHFQze8A
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


