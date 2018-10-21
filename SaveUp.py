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

data = '''\
QlpoOTFBWSZTWW8ludUACVJf4VVQVGd/9b/nna6/79/+QAAAIBAAYAd/B5ZNLsrsUAPuAA
AewymU1HqntU8U9qnsigyAAAGgAAAADQjQ0AjJTSnqAAAZGQAAAABxkyaGIxNGARgJhAGA
mmjTI0AwkUyqek9TTQAAAAGgAADQAADKUZBpoDQA0AA0PUAA0AABoIlEyJo0jJoaQjQZMg
ZB6mQAYBNpBdHapEVDxo6Punv2USuFD8mIVY2bNasIBaBIyFkYqFUYjojZ7XGgFmyBIjCE
CAEioQiGOOpFHVEQEdSogWpQ7iAhWsSh6qA0IEAh5oA1ihUi0maIjl+s89wA9Pr889Rglz
5fNw5LIC0gClq3u6mFvmviWcm+sW6vjB9it08hNDIpMSDCGpgiVQEwx0TCJYNgSRQijbE0
2TQjIgFSCVKIFwSIG5f77ngOEq1SyBGTLs+zwwlpvEFAdGytzeGxuKSNo8kFt9Kat54KcC
2DIxZzh6cZGrK4Nutw2qKxmDCw2CSIHsMWPzQQCNch9P1vjRqeIsVKkkGDCEIWs+MKiXIA
2takLODUYBEhcG+FZAZgje7csQZQkFNKSpFUyppNobhICwZ6+4b00WFmFj06U78aEGrRoJ
BII0RojQQ8hylCxBA6Y99IEIiQwyF6q9471cDjewYWoZDUTE3UhqQSoQWamrsZF6gC+VbU
Mpl1WXSuOcezTn3GCKdoVSiZSuQeUor5She7WcnuhsVwERsXSlTST4dAOWMCBYlHUTGSI7
J5TrCDQbmwm11Dctvzt5PHIeTgcCmSmmwNCoOrBSYBgXMp31CB6bv+Vlv1Inlxuu17RfNP
OgZUOwL2B6JuHca916c1MB6TeM5N7xCwQhpRrxOmo2IO+hzVS9S5aJTTsJYEmdYRJQXuoR
uWuULmrG3UWVM8LahUIEQMkI83fF4UsM4O04TzCAIzENbaryg+ASqAVm9NSpe4AHfpwm6X
XCtbfA5hegAHJiHPgwlqoFCRiCLJun2yL9FEhN5BTvbZ1PapXtYXD1oltpwDkd56nzUZMl
gw3w59kW3mTsQGCimUYrAFtdLGq0l0SIpVwxCTwhEbRcNqnFqFw++6Urfk+qrcAco1iEXO
iNPOuTOe1HSwacUtk8zatopMt4m8rgYG0KStgJc7wBQlacgcX61FjWLRkc6rgxeljcQCtJ
3cSqeK9cRw1F0tNuYVp1Adb5hxNDwr6kI4lHhYPxlQzpZrRIzBRHXCC2E3U1u+5IHAaIEC
Be3Mh/BDuauyG8dnYENao4+B0ezTTutxk9qJE27GJWSoh9wH1uMcYxTijOu43ccxjznk4H
fMbdr6X6iELOyZyCYMelQCYni7szh1HWX2i9F0zihMKnNVd5APDVKi+o5Pni7Ot1jHMl2z
tCk44dXNr2vqtBN1IyOrOOb8PeMsuRPjjN1NqTtCeaPxi164TCPi7sQ/IaLwMiJvf9r1h3
qCBgwWyEEG0CgB2QBbTKQwlJSQb9OvpYMasqYgLQQNgwGhYoJ5QOzhUD6Adg+gOLge1u+1
6DlfFcsPIrXJU2qBrQDcBM3FAw9WuSG/B3CGhEKe4EkxApViAZJ63ggYAYNwCqjo1AuY7U
C2w80JFMewvs5IBIqnvExfRgSH8nOQaIFECORRPZ4ODmXdDnCPvOU6hCqBxNa8/ObdaPJD
UXx1FHgVQKIGmXZQxK03zpQPtopiPu6nwq7kHcRANbt7bNYVQg32Ye1hkVDuAmnbAOxHcG
ssWHQhyliCZ5lDm6RNXSzeQGEHeaxwQDbkdAXQI2e1Uqd1TJdhmlADmumeD2HRUuAvRs6N
4wDUY6lPeSFW+wYAZvexDGF8hugYOswAtUAoMCGRs3dU1GiBtucQ4JcNbCMeujzAFA6k57
G8yZ0gShfl4SG9Ka460A7xuuBf79gJ0ECzQomRNBDuwCRaVRDgXpKPDHeAZ0BOAh0oBlzJ
tbV53P3JJE+N5pCleWiBmBkbOrMzQLpinOU2AmQ3JddUoXOUyd4+HdQE1hZIaxzRNDilQC
+dyzjpRDR6gTrScgBh/uj1Z0tqaEQLkr39+GAhxvoF02iUPUx9iMR84xCDBgyDCECMkQjN
aAfn5tMcW/sQDrwOtsJ1ou9V+NwuHiKl0TRO45ajqHJLlWCGKokmjHAAccqfxdyRThQkG8
ludUA=
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
#v['Congratulations'].hidden = False
#v['Congratulations'].bring_to_front()

#v['meetinggoalsegment'].action = segmented_action
#v['button1'].action = segmented_action

#av = ui.load_view()
v.present('sheet')


