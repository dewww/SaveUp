#import requests
#import pprint
#import time
import json

data = '''\
QlpoOTFBWSZTWXoBYuAABWlf4VUQVGd/9b+nmaq/79/+QAAAIBAAUAReOttdQB3vFKEMlE
0NNDQ0NAAAwgAAAAANECY0aIyinqZMgAAAyAAAAJIJU9Rk09QAPU0AAAZDQAAACKVT01PU
8jTJGIAAAAAAAeoBoIlFPRGiT0ZBAaaaAA0AaaMRiek9QWR2FIiIepDM9c15aVgOL5IUUa
oRDMhZCgtSCQYhII2tdeKCt4IJ3BRLki8tEA6MAVcfHLlD89PNOjEWODl4c9BFxIHxdq+w
dzP8W8j2bxUCYd3B5JEslQ6GkLLGRijQSykEwTVveB2OlCqEXi29OR59VkIqs8s+y+wJMF
LOGj3VxsMmchaIDZBIdJvOkB0l0pSYYmRwB4HQMlIKYQQgmQggCsouKIYlDta4TK2an4yb
9QoBBCqFEHEjRZmZDAlXXF59B7EqFLL1JTQmshKrDtJAVKJk8xypM/QOnLWTVnVZM53tTl
5xKlQcpVejGcVVJgYLjoT8zGIV0Spbi/vsxKR0MCl0irHrnGapLQ33ZzY6Ry5jmCu1RjQG
VzIr2D2vDratInCuItItcbsjLXW7TKzwgrQUW7g4qnE8yrAigYfpuaDswCcb0YEBFdboNJ
Aio5NYFN7BwOnDZ2BJYwmVmMBnc9yTWtYUeIR498dEkRHm1yKFXUbkixqmmIAhBY72hlNs
kjm3S2IW3I48WPV2qCMLVQlYwLWom2FDdB1cOEco0iQ1jrCK50rojnh6ocaya9Z7No6cE2
Q9CLNmvrGJgYAIiLrxBfgFnTUlm3hSLThTJnd8Hu1OGTKIck8UOmKTe7ala+omTbuMLAXm
yt5Iy8xA95h0QzuAb9J8LRs/WwwmW7bbbBaTRFpmSyVYNULTQrMxiM7R2F0kyICl8ttAAQ
rtqbsCwCiAawUKgItuOEDUvcqIFoF1F7LNeWle1CSVAnUJlCUTz5YjnksFJqUlIofp6PgJ
ZCIGXLmErhywC3WXd0ENa3bImgSXFA6dV5ZwNIQzbiJQTGOjDGjzwxdlSCYdeBfp9Fm5dW
5wIbAIZHdMjQCLa9rIcwS3lofUjItFLbvX1pv1GMLBC6GQtpQqJu1e9vtwF7BLhz0BDRfm
XaA034t9Yhj12LXLYSiFcBaJAhu6LjATLthtOcX0hgcqeomglrbrdqihQk3pxLzAVw4FCJ
kSuWpDHKA6V21DON+jqHbkA1mzIVqrrsJQM4zSJmXITP+9oS4KkOwJtG6ZENyt2FN4TKhT
+5HelxiilLw4RyLQ6UIhzxSEiEYwgQwUPp8dN1upQ4qgcSHHzc5RaTDm5JScll8WGIDFiz
/8XckU4UJB6AWLgA==
'''
import ui
import bz2
from base64 import b64decode
pyui = bz2.decompress(b64decode(data))
v = ui.load_view_str(pyui.decode('utf-8'))

# ------------------------

#v['imageview1'].image=ui.Image.named('photo.jpg')

v.name = '$aveUp^'

def segmented_action(sender):
#	if sender.segments[sender.selected_index] == 'meetinggoalsegment':
	sender.selected_index = 0 #reset 
	v['saveuptosegment'].selected_index += 1

segmented = v['meetinggoalsegment'] # Determine if it is the meetinggoalsegment control
segmented.action = segmented_action

#av = ui.load_view()
v.present('sheet')


