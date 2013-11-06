# -*- coding: utf-8 -*-

import requests
import json
import nltk
from nltk.tokenize import LineTokenizer
import csv
import time
import pprint
from unidecode import unidecode

devkey = (open('dev_key.txt','r')).read()

text = open('keywords.txt','a')
for y in range(2010, 2014):
    for m in range(1,13): # first number is starting month, last number needs to be one more than final month
        url = 'http://labs.adsabs.harvard.edu/adsabs/api/search/?q=bibgroup:cfa,pubdate:'+str(y)+'-'+str(m)+'&rows=200&fl=keyword&fmt=json&dev_key='+str(devkey)
        #print url
        content = requests.get(url)
        k=content.json()
        #pprint.pprint(k)
        docs = k['results']['docs']        
        for i in docs:
            try:
                mywords=i['keyword']
                myList = list(set(mywords)) #magic line that removes exact duplicates from an articles keywords
                myList2 = str(y)+'|'+str(m)+'|'+('\n'+str(y)+'|'+str(m)+'|').join(myList)
                cleanmyList = myList2.encode('ascii', 'ignore') #ignores ascii characters
                text.write(cleanmyList+'\n')
            except KeyError:
                #this error occurs when the paper has no keywords
                pass
        time.sleep(1)
text.close()
print 'finished getting keywords'

text = open('keywords.txt','r').read()
freqlist = open('freqlist.txt','wb')
lowertext = text.lower()
lines = LineTokenizer(blanklines='discard').tokenize(lowertext)
freq = nltk.FreqDist(lines)
#print freq
writer = csv.writer(freqlist, delimiter='|', lineterminator='\n', quotechar='"', quoting=csv.QUOTE_MINIMAL)
writer.writerows(freq.items())
freqlist.close()
print 'finished getting frequency distribution'

out = open('frequency.csv', 'w')
csv_out = csv.writer((out), lineterminator='\n', delimiter=',')
csv_out.writerow(["Year","Month","Keyword","Frequency"])
f = open('freqlist.txt')
for line in f:
  vals = line.split('|')
  words = [v.replace('\n', '') for v in vals]
  words1 = [v.replace('"', '') for v in words]
  csv_out.writerow((words1[0], words1[1], words1[2], words1[3]))
f.close()
out.close()
print 'finished writing csv file'