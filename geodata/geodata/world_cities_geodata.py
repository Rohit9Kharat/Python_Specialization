import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else :
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

conn = sqlite3.connect('world_cities_geodata.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS All_Cities (address TEXT, country TEXT, state TEXT, district TEXT, city TEXT, postal_code TEXT, latitude TEXT, longitude TEXT, geodata TEXT)''')


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("world_cities.data", encoding="utf8")
count = 0

for line in fh:
    if count > 200 :
        print('Retrieved 200 locations, restart to retrieve more')
        break

    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM All_Cities WHERE address= ?",
        (memoryview(address.encode()), ))

    try:
        data = cur.fetchone()[0]
        print("Found in database ",address)
        continue
    except:
        pass

    parms = dict()
    parms["address"] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1

    try:
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print('==== Failure To Retrieve ====')
        print(data)
        break

    format_address = js['results'][0]['address_components']

    for index in format_address:
        if index['types'][0] == 'locality':
            city = index['long_name']
        else:
            city = None

    for index in format_address:
        if index['types'][0] == 'administrative_area_level_2':
           district = index['long_name']
        else:
            district = None

    for index in format_address:
        if index['types'][0] == 'administrative_area_level_1':
            state = index['long_name']
        else:
            state = None

    for index in format_address:
        if index['types'][0] == 'country':
            country = index['long_name']
            #print(country)
        else:
            country = None
            
    for index in format_address:
        if index['types'][0] == 'postal_code':
            postal_code = index['long_name']
        else:
            postal_code = None

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']

    cur.execute('''INSERT INTO All_Cities (address, country, state, district, city, postal_code, latitude, longitude, geodata)
            VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ? )''', (memoryview(address.encode()), country, state, district, city, postal_code, lat, lng, memoryview(data.encode())))
    conn.commit()
    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
