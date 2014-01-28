# -*- coding: utf-8 -*-

import requests
import json
import csv
import time
import codecs
import cStringIO

#UnicodeWriter from http://docs.python.org/2/library/csv.html#examples
class UnicodeWriter:
    def __init__(self, f, dialect=csv.excel, encoding="utf-8-sig", **kwds):
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()
    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        data = self.encoder.encode(data)
        self.stream.write(data)
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)

#/end UnicodeWriter

devkey = (open('dev_key.txt','r')).read() #txt file that only has your dev key

bibcodes = open('bibcodes.txt').read() #one bbicode per line
bibcode_lines = bibcodes.splitlines()

resultFile = open("checkaffil.csv",'wb')
wr = UnicodeWriter(resultFile,dialect='excel',quoting=csv.QUOTE_ALL)

for i in bibcode_lines:
    url = 'http://labs.adsabs.harvard.edu/adsabs/api/record/'+i+'?fmt=json&dev_key='+str(devkey)
    print url #printing url for troubleshooting
    content = requests.get(url)
    k=content.json()    
    
    wr.writerow(['%R']+[i]) #write the bibcode
    
    try:
        title = k['title']    
        wr.writerow(['%T']+title)
    except KeyError:
        wr.writerow(['%T'])

    try:
        authors = k['author']   
        wr.writerow(['%A']+authors)
    except KeyError:
        wr.writerow(['%A'])
    
    try:
        affil = k['aff']   
        wr.writerow(['%F']+affil)
    except KeyError:
        wr.writerow(['%F'])
    
    wr.writerow([''])
    time.sleep(1)
    
resultFile.close()
print 'finished getting data, look at checkaffil.csv'