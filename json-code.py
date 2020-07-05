#Week 6 Assignment 1

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
	url = input('Enter location: ')
	print('Retrieving', url)
	uh = urllib.request.urlopen(url, context=ctx)
	data = uh.read().decode()
	print('Retrieved', len(data), 'characters')

	js = json.loads(data)
	
	#print(json.dumps(js, indent=4))

	summ=0
	for i in range(0,len(js["comments"])):
		summ=summ+int(js["comments"][i]["count"])
	
	print('Sum is : ',summ)

