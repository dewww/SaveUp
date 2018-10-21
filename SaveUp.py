#import requests
#import pprint
#import time
import json

data = '''\
QlpoOTFBWSZTWY/tLtAABaDf4VUQVGd/9b+nmaq/79/+QAAAIBAAUAReCjegBYoDhkojI0
DRoAAAMgADQ0AA0GiAA0JlFPUNAAAAyHqAAADjJk00wmRkDAjE0YIwg0aYABBFRGqH6p6n
6oADQAB6gANNAA0ABEoIjRHpMmimnpPU00B6QHqaAHqeo8U/Sn6oLo8ikBUPoQ1vnOOqlY
Db70KKNUIhrQuhQWpACDBJBG98MVFVxUROpFTBIvdRAPDJQA0flMFD+fH954WLnq7vXncT
kUKa/mPkD9ocNXN5TvajClLVCtAsLA2tapJC6xkYo0EupBMk4dPwPJ4oVQITHalZm3FcDI
gLNrOLssExBJXSzjo+FcsWQZ6FogTgCHsX5exDsLUWywhaxRUpUohFsDaqFULWCpUCsoto
hZQ9HGE1N2p/GnrqFAIIVQohRA6RgyAhnnXtp6KdS3L9XbezBZdJZE+EiICpQMmmOScT9A
6kcRWkqpFXM1c+nzCNKg5zpKyMblMVgEApFGPLAmY0llZVz2wgVqdMAa1EQfezEN87O33V
y55DjynIFdaDLwZXMivYNW0MthZEwVzBZFjO7Q0tlu2qsszFaCiXYGFU4HqNXETjDX7lg7
KAlC9FCYIrpeYfEEVGTw4pNUOB04bMyIpB0ispQM7nunJK1dRodDo74PnEiPVrkTqsovRF
nE35cCDkhvWFU20U2LvO2XW3TYebHhmJiDrVmSKUErUSW6hscyuWCGprIpmkMOgmn1fNjQ
1JnCsVtSW1GMk6e0zcRasttYQMDJEAAOxAF+AWn4JJL4Ugs3U0Z3a5rMG7RlAcQ01e8BVa
bkNNyUazSWtxJUl84xhw2kqu0ZqvIOPgYZAK74HB8uhaFm4sMz0vbbbYJSU5pTUUiiOWgS
jysrOYSsk4ni7Fby4ZBAP7va3sABmBxDBiJt22oXsLc04C6oust6/syovYhVJAmoYqFxO/
tk9tfIUnBSUih/T4e0S6EQNWrWJXu1IX8zD0ghxXDYJtEmBQPHhiXcjcENe9EoJoHbloR7
4W9xSCZeeRju9lxMF4b/UhRRJuaTYgQWv1vwc8SzOQ+ampcOjZkZa058ygsIvp0LZQqJ0V
fe6xMAMWCYDnQENuOteYDdjbrWIaONy+C3EohXIWiQIdG3AyE1c4czmL84b3dpzMYX2PK8
ucyUK+zSJzMDZHeoTFE2XzE0UB3LzqGY47fIeeQDibJCtVeNxKBmM3Ca10kz/vmEwCpDlE
2HQaUN9cMqdImpCn+6XpmBaCFMQ9Y6VoeKEQ74pCRCMYQIZKH4/duwv5KH11AyEDa9yChK
iMPOoojsEniUKIA+/S/i7kinChIR/aXaA=
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


