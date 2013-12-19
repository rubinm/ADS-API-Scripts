# -*- coding: utf-8 -*-

import requests
import json
import csv
import time
from unidecode import unidecode

devkey = (open('dev_key.txt','r')).read() #txt file that only has your dev key

authors = open('authors.txt').read() #one author per line, in format: Kurtz,+M
authors_lines = authors.splitlines()
out = open('articles_out.txt', 'w')

for i in authors_lines:
    for y in range(2010, 2011): #year range you wish to scrape, the ending number should be one more than your final year (i.e. range(2010,2014) will get info on years 2010, 2011, 2012, 2013)
        for m in range(1,2): #first number is starting month, last number needs to be one more than final month
            url = 'http://labs.adsabs.harvard.edu/adsabs/api/search/?q=bibgroup:cfa,author:"'+i+'",pubdate:'+str(y)+'-'+str(m)+'&filter=property:not_refereed&rows=200&fmt=json&dev_key='+str(devkey)
            #above api request finds only CfA bibliography non-refereed papers.
	    print url #printing url for troubleshooting
            content = requests.get(url)
            k=content.json()
            
            docs = k['results']['docs']
            for x in docs:
                bibcode=x['bibcode']
                pubdate=x['pubdate']
                
                try:
                    affil=x['aff']
                    affillist = unidecode(('; ').join(affil))
                except KeyError:
                    affillist = ''        
                
                try:
                    title=x['title']
                    titleclean = unidecode(('').join(title))
                except KeyError:
                    titleclean = ''
                
                try:
                    pub=x['pub']
                except KeyError:
                    pub = ''
                    
                try:
                    database=x['database']
                    databaseclean = ('').join(database)
                except KeyError:
                    databaseclean = ''
                
                try:
                    author=x['author']
                    authorlist = unidecode(('; ').join(author))
                except KeyError:
                    authorlist = ''
                
                try:
                    year=x['year']
                except KeyError:
                    year = ''                              
                
                row = bibcode+'|'+year+'|'+str(m)+'|'+authorlist+'|'+affillist+'|'+titleclean+'|'+databaseclean+'\n'
                #print row
                out.write(row)    
        time.sleep(1)
out.close()
print 'finished writing text file'

print 'starting de-duping'
uniqlines = set(open('articles_out.txt').readlines())
#print uniqlines
dedupe = open('articles_out_dedupe.txt', 'w')
uniquelines = ('').join(uniqlines)
dedupe.write("Bibcode|Year|Month|Authors|Affiliation|Title|Database"+"\n")
dedupe.write(uniquelines)
dedupe.close()
print 'finished'

print 'writing as CSV'
out = open('articles_out.csv', 'w')
csv_out = csv.writer((out), lineterminator='\n', delimiter=',')
f = open('articles_out_dedupe.txt')
for line in f:
  vals = line.split('|')
  words = [v.replace('\n', '') for v in vals]
  words1 = [v.replace('"', '') for v in words]
  csv_out.writerow((words1[0], words1[1], words1[2], words1[3], words1[4], words1[5], words1[6]))
f.close()
out.close()
print 'finished writing csv file'
print 'Results: articles_out.csv'
