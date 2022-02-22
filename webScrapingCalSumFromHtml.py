'''
Created on 05-Jul-2020

@author: Rohit Kharat
'''

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")


# Retrieve all of the anchor tags
webScrapStringIntList = list()
numList = list()
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print(type(tag.contents[0]))
    #print('Attrs:', tag.attrs)
    webScrapStringIntList.append(tag.contents[0])
#print(webScrapStringIntList)
    
for i in range(len(webScrapStringIntList)):
    num = int(webScrapStringIntList[i])
    numList.append(num)
print(sum(numList))