#Week 5 Assignment
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
# Ignore SSL certificate errors


url = input('Enter URL:')
response = urllib.request.urlopen(url)
tree = ET.fromstring(response.read())
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data), 'characters')
lst = tree.findall('comments/comment')
print('Count:',len(lst))
total = sum([int(count.text) for count in tree.findall('comments/comment/count')])
print(total)
