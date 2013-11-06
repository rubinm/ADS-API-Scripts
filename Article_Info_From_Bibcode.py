# -*- coding: utf-8 -*-

import requests
import json
import time
from unidecode import unidecode

devkey = (open('dev_key.txt','r')).read()

#you need to start with a text file containing a list of bibcodes
bib = open('cfa_bib_list.txt').read()
w = open('abstract.txt','w') #will create or overwrite this file name

bib1 = bib.splitlines()
bib_lines = [x.strip() for x in bib1]

for i in bib_lines:
    url = 'http://labs.adsabs.harvard.edu/adsabs/api/record/'+i+'?fmt=json&dev_key='+str(devkey)
    
#this section resets each variable to blank every time the script runs through the loop
    authors = ''
    title = ''
    affil = ''
    year = ''
    pub = ''
    abstract = ''
    
    content = requests.get(url)
    k=content.json()

    year = k['year']
    w.write(year+'|')
    
#these "try,except" pairs will try to get the information from the article, but if it doesn't exist will just pass the blank variable as assigned above
    try:
        pub = k['pub']
        w.write(pub+'|')
    except KeyError:
        w.write(pub+'|')
    
    try:
        title = k['title']
        title2 = '; '.join(title)
        cleantitle = title2.encode('ascii', 'ignore') #this ignores non-ascii characters
        w.write(cleantitle+'|')
    except KeyError:
        w.write(title+'|')
    
    try:
        authors = k['author']
        author2 = '; '.join(authors)
        cleanauthors = author2.encode('ascii', 'ignore')
        w.write(cleanauthors+'|')
    except KeyError:
        w.write(authors+'|')
 
    try:        
        affil = k['aff']
        affil2 = '; '.join(affil)
        cleanaffil = affil2.encode('ascii', 'ignore')
        w.write(cleanaffil+'|')
    except KeyError:
        w.write(affil+'|')
    
    try:
        abstract = k['abstract']
        cleanabstract = abstract.encode('ascii', 'ignore')
        w.write(cleanabstract+'|')
    except KeyError:
        w.write(abstract+'|')

    print i #prints the bibcode as the script runs in order to track progress and locate errors
    
    w.write(i+'\n')  #the last variable write needs to end with a \n instead of the delimiter |
    
    time.sleep(2)
print 'finished getting the informtion'
w.close()