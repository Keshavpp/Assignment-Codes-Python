#Week 4- assignment2
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
#Code to get the anchor tag links 

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

ls = input('Enter url-')
count = input('Enter count - ')
pos = input('Enter position - ')
count = int(count)
pos = int(pos)
tada = list()
for i in range(count):
	url = ls
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	# Retrieve all of the anchor tags
	
	tags = soup('a')
	f = 0
	for tag in tags:
		x = tag.get('href', None)
		f = f+1
		if(f ==pos):
			ls = x
			y = tag.contents[0]
			tada.append(y)
			break
print(tada)