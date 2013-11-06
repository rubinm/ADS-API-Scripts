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

bib = open('cfa_bib_list.txt').read()
w = open('abstract.txt','w')

bib1 = bib.splitlines()
bib_lines = [x.strip() for x in bib1]

for i in bib_lines:
    url = 'http://labs.adsabs.harvard.edu/adsabs/api/record/'+i+'?fmt=json&dev_key='+str(devkey)
    
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
    
    try:
        pub = k['pub']
        w.write(pub+'|')
    except KeyError:
        w.write(pub+'|')
    
    try:
        title = k['title']
        title2 = '; '.join(title)
        cleantitle = title2.encode('ascii', 'ignore')
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

    #print abstract
    #print authors
    #print title
    #print year
    print i
    
    w.write(i+'|\n')
    
    time.sleep(2)
print 'finished'
w.close()