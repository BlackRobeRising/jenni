"""roll

REQUIRES:
	requires: git clone git@github.com:5monkeys/pyparsing.git

TODO: 
	second  d = drop
	re-roll r = re-roll based on next #
	exploding e = roll a second die of the same size if it is that # or above

	automatically sort dice from lowest to highest die	
"""

import HTMLParser
import re
from socket import timeout
import string
import web
import json
import urllib2
import imp

def perform_throw(uri, roll_string, jenni):
        q = roll_string.encode('utf-8')
        q = q.replace('\xcf\x95', 'phi')  # utf-8 U+03D5
        q = q.replace('\xcf\x80', 'pi')  # utf-8 U+03C0
	answer = urllib2.urlopen(uri + web.urllib.quote(q))
	j = json.load(answer)
	print j
	return j["string"]


def throw(jenni, input):
	c = imp.load_source('colors', './modules/colors.py')
	irc_colors = c.irc_colors()

	roll_string = input.group(2)

	if not input.group(2):
        	return jenni.reply('Nothing to calculate.')
	uri = "http://10.1.1.2/unstable/dice/roll/request.json?format=irc&dice_string="
	#uri = "http://dev.local/unstable/dice/roll/request.json?format=irc&dice_string=" #outside VM

#	jenni.say(uri + roll_string)

	jenni.say(irc_colors.GREEN+input.nick+irc_colors.NORMAL+' : ' + perform_throw(uri, input.group(2), jenni ))
	
throw.commands = ['throw', 'roll', 'r']
throw.priority = 'medium'
