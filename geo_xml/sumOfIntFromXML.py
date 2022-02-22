'''
Created on 06-Jul-2020

@author: Rohit Kharat
'''
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')

    if len(address) < 1:
        break

    parms = dict()
    parms['address'] = address

    if api_key is not False:
        parms['key'] = api_key

    #url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', address)

    uh = urllib.request.urlopen(address, context=ctx)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    #print(data.decode())
    #data.decode()
    tree = ET.fromstring(data)

    counts = tree.findall('comments/comment')
    break
    #print(counts)
listInt = list()
for item in counts:
    #listInt.append(lst[i])
    listInt.append(int(item.find('count').text))
print(sum(listInt))
