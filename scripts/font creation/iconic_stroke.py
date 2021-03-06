#Copyright (C) 2012  P.J. Onori (pj@somerandomdude.com)

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

#!/usr/bin/env python

import fontforge
import json
from pprint import pprint
json_data=open('iconic_stroke.json')

data = json.load(json_data)

font = fontforge.open('blank_stroke.sfd')

for file_name, char in data.iteritems():
	c = font.createChar(int("0x" + char, 16))

	c.importOutlines('../../vector/' + file_name + '.svg')

	c.left_side_bearing = 15
	c.right_side_bearing = 15

#font files

font.generate('iconic_stroke.svg')
font.generate('iconic_stroke.ttf')
font.generate('iconic_stroke.eot')
font.generate('iconic_stroke.otf')

#css file

theString="@font-face { font-family: 'IconicStroke'; src: url('iconic_stroke.eot'); src: url('iconic_stroke.eot?#iefix') format('embedded-opentype'), url('iconic_stroke.ttf') format('truetype'), url('iconic_stroke.svg#iconic') format('svg'); font-weight: normal; font-style: normal; }"
theString+=".iconic { display:inline-block; font-family: 'IconicStroke'; }"
for file_name, char in data.iteritems():
	theString += "." + file_name + ":before {content:'\\" + char + "';}"

f = open("iconic_stroke.css", 'w')
f.write(theString)
f.close()

#html file
theString="<html><head><title>Iconic Font-embedding demo</title><link rel='stylesheet' href='iconic_stroke.css' type='text/css' media='screen' /><style> body {font-family:'Helvetica', arial, sans-serif;} span { font-size:36px; }</style><body>"
theString += "<table><tr><th>Name</th><th>Iconic Icon</th><th>Unicode Icon</th><th>Hexidecimal Code</th>"
for file_name, char in data.iteritems():
	theString += "<tr><td>" + file_name + "</td><td><span class='iconic " + file_name + "'></span></td><td><span class='" + file_name + "'></span></td><td>" + char + "</td></tr>"

theString += "</table></body></html>"

f = open("iconic_stroke_demo.html", 'w')
f.write(theString)
f.close()
