#import requests
#import pprint
#import time
import json
	
def weekly_total_action(sender):
	v['view1'].send_to_back()
#	v['view1'].hidden = True
	v['Transactions'].bring_to_front()
	v['Transactions'].hidden = False
#	v['Transactions'].present('popover') #,hide_close_button=False)
	
def txn_detail_action(sender):
#	sender.tableview.superview['tableview1'].hidden = True
#	sender.tableview.superview['tableview1'].send_to_back()
#	sender.tableview.superview['tableview2'].hidden = True
#	sender.tableview.superview['tableview2'].send_to_back()
#	sender.tableview.superview['textview1'].hidden = False
#	sender.tableview.superview['textview1'].bring_to_front()
	reset_view(sender)
			
def sweep_action(sender):
	v['view1'].send_to_back()
#	v['view1'].hidden = True
	v['Congratulations'].bring_to_front()
	v['Congratulations'].hidden = False
	v['Congratulations'].present('popover') #,hide_close_button=False)
	
def reset_view(sender):
	v['view1'].bring_to_front()
	v['view1'].hidden = False
	v['Transactions'].send_to_back()
	v['Transactions'].hidden = True
	v['Congratulations'].send_to_back()
	v['Congratulations'].hidden = True

def hide_splash(sender):
	sender.hidden=True
	sender.send_to_back()
	v['view1'].bring_to_front()
	v['view1'].hidden = False

def segmented_action(sender):
#	if sender.segments[sender.selected_index] == 'meetinggoalsegment':
	sender.selected_index = 0 #reset 
	v['view1']['saveuptosegment'].selected_index += 1
	if v['view1']['saveuptosegment'].selected_index <= 0:
		v['view1']['imageview1'].hidden = True	
		v['view1']['imageview1'].image = ui.Image.named('CreditScore.PNG')
		v['view1']['imageview1'].hidden = False
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
v['view1'].hidden=False
#v['view2'].send_to_back()
#v['view2'].hidden=True
#v['view2']['button1'].image = ui.Image.named('SelectSite.png')
#v['view2']['button1'].image = ui.Image.named('IMG_0420.PNG')
v['view2'].hidden=True
#v['view2'].hidden=False
v['Transactions'].hidden = True
v['Congratulations'].hidden = True
v['Congratulations']['imageview1'].image = ui.Image.named('IMG_0417.PNG')
#v['view1']['imageview1'].image = ui.Image.named('IMG_0420.PNG')
print('IMG_042'+format(v['view1']['saveuptosegment'].selected_index)+'.PNG')
#v['Congratulations'].hidden = False
#v['Congratulations'].bring_to_front()

#v['meetinggoalsegment'].action = segmented_action
#v['button1'].action = segmented_action

#av = ui.load_view()
v.present('sheet')


