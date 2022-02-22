'''
Created on 05-Jul-2020

@author: Rohit Kharat
'''
'''
Created on 05-Jul-2020

@author: Rohit Kharat
'''
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from networkedTech import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html1 = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html1, 'html.parser')

# Retrieve all of the anchor tags
htmlList = list()
tags = soup('a')
for tag in tags:
    #print(tag.get('href', None))
    htmlList.append(tag.get('href', None))
#print(htmlList[2])
sec_link = htmlList[17]
htmlList = []
    
html2 = urllib.request.urlopen(sec_link, context=ctx).read()
soup = BeautifulSoup(html2, 'html.parser')
tags = soup('a')
for tag in tags:
    htmlList.append(tag.get('href', None))
third_link = htmlList[17]
htmlList = []

html3 = urllib.request.urlopen(third_link, context=ctx).read()
soup = BeautifulSoup(html3, 'html.parser')
tags = soup('a')
for tag in tags:
    htmlList.append(tag.get('href', None))
fourth_link = htmlList[17]
htmlList = []

html4 = urllib.request.urlopen(fourth_link, context=ctx).read()
soup = BeautifulSoup(html4, 'html.parser')
tags = soup('a')
for tag in tags:
    htmlList.append(tag.get('href', None))
fifth_link = htmlList[17]
htmlList = []

html5 = urllib.request.urlopen(fifth_link, context=ctx).read()
soup = BeautifulSoup(html5, 'html.parser')
tags = soup('a')
for tag in tags:
    htmlList.append(tag.get('href', None))
sixth_link = htmlList[17]
htmlList = []

html6 = urllib.request.urlopen(sixth_link, context=ctx).read()
soup = BeautifulSoup(html6, 'html.parser')
tags = soup('a')
for tag in tags:
    htmlList.append(tag.get('href', None))
seventh_link = htmlList[17]
htmlList = []

html7 = urllib.request.urlopen(seventh_link, context=ctx).read()
soup = BeautifulSoup(html7, 'html.parser')
tags = soup('a')
for tag in tags:
    htmlList.append(tag.get('href', None))
eight_link = htmlList[17]
htmlList = []

split1 = eight_link.split("_")
split2 = split1[2].split(".")
print(split2[0])

#http://py4e-data.dr-chuck.net/known_by_Arooba.html