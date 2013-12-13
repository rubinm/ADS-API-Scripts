# -*- coding: utf-8 -*-

import requests
import json
import time
from unidecode import unidecode

devkey = (open('dev_key.txt','r')).read() #txt file that only has your dev key

authors = open('authors.txt').read() #one author per line, in format: Kurtz,+M

authors_lines = authors.splitlines()

out = open('articles_out.txt', 'w')
out.write("Bibcode|Year|Month|Authors|Affiliation|Title|Database"+"\n")

for i in authors_lines:
    for y in range(2010, 2011): #year range you wish to scrape, the ending number should be one more than your final year (i.e. range(2010,2014) will get info on years 2010, 2011, 2012, 2013)
        for m in range(1,2): #first number is starting month, last number needs to be one more than final month
            url = 'http://labs.adsabs.harvard.edu/adsabs/api/search/?q=bibgroup:cfa,author:"'+i+'",pubdate:'+str(y)+'-'+str(m)+'&filter=property:not_refereed&rows=200&fmt=json&dev_key='+str(devkey)
            #above api request finds only CfA bibliography non-refereed papers.
            
            content = requests.get(url)
            k=content.json()
            
            docs = k['results']['docs']
            for x in docs:
                #caputre all desired information
                bibcode=x['bibcode']
                pubdate=x['pubdate']
                affil=x['aff']
                title=x['title']
                pub=x['pub']
                database=x['database']
                author=x['author']
                year=x['year']

                #converting lists into strings, and cleaning up unicode where needed
                databaseclean = ('').join(database)
                titleclean = unidecode(('').join(title))
                authorlist = unidecode(('; ').join(author))
                affillist = unidecode(('; ').join(affil))              
                
                #putting all the variables together into one long string
                row = bibcode+'|'+year+'|'+str(m)+'|'+authorlist+'|'+affillist+'|'+titleclean+'|'+databaseclean+'\n'
                print row #print each string for error tracking
                out.write(row) #write each line to the txt file
        time.sleep(1)
out.close()
print 'finished writing text file'