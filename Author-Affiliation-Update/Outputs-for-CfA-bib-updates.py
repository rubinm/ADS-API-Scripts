# -*- coding: utf-8 -*-

import os
import csv
import string
from datetime import datetime

#Rahul's script for interating the alphabet for the affiliations

allTheLetters = string.ascii_uppercase
standard_mapping = list(allTheLetters)

def alphabets2(affiliations):
    outs=[]
    N=len(affiliations)
    maxmodulus = N / 26
    maxsecondletter =  N % 26
    if N % 26 ==0:
        howmanytimes=range(maxmodulus)
    else:
        howmanytimes=range(maxmodulus+1)
    j=0
    for i in howmanytimes:
        firstletter = standard_mapping[i]
        if i==(len(howmanytimes) - 1 ) and maxsecondletter!=0:
            letters = [firstletter+standard_mapping[k] for k in range(maxsecondletter)]
        else:
            letters = [firstletter+standard_mapping[k] for k in range(26)]
        for l in letters:
            out = l+'('+affiliations[j]+')'
            outs.append(out)
            j=j+1
    return outs

#/end Rahul's script

#This creates and writes a file called "updates(timestamp).txt" that will list all author/affiliation updates marked on checkaffil.csv

updates = open('updates'+datetime.now().strftime("%Y_%m_%d_%H%M")+'.txt', 'w')

with open('checkaffil.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        #print row
        if '%Rc' in row:
            row.pop(2)
            joined = ''
            bib = (', ').join(row)
            bibcodes = bib.replace('%Rc,','%R')
            data=bibcodes.strip(", ")
            print data
            updates.write(data+'\n')  
            
        elif '%Ac' in row:
            joined = ''
            auth = ('; ').join(row)
            authors = auth.replace('%Ac;','%A')
            data=authors.strip(", ")
            print data
            updates.write(data+'\n')
            
        elif '%Fc' in row:
            a=row
            #print a
            a.pop(0)
            outside=[]
            h=alphabets2(a) #uses Rahul's above function
            h=[e for e in h if e[-2:]!='()'] #more code from Rahul!
            data =  ['%Fc']+h
            joined = ''
            affil = (', ').join(data)
            data = affil.replace('%Fc,','%F')
            print data
            updates.write(data+'\n')
            
            updates.write('\n')

updates.close()


#This creates and writes a file called "bibs(timestamp).txt" that will list all bibcodes marked on checkaffil.csv

bibfile = 'bibs'+datetime.now().strftime("%Y_%m_%d_%H%M")+'.txt'
bibs = open(bibfile, 'w')

with open('checkaffil.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        
        if '%Rc' in row:
            try: 
                if 'x' in row[2]: #checks to see if any are marked for bibcode
                    row.pop(2)
                    bib = (', ').join(row)
                    bibcodes = bib.replace('%Rc,','')
                    data=bibcodes.strip(", ")
                    print data
                    bibs.write(data+'\n') #writing bibcode
            except IndexError:
                pass
        
        if '%R' in row:
            try:
                if 'x' in row[2]: #checks to see if any are marked for bibcode
                    row.pop(2)
                    bib = (', ').join(row)
                    bibcodes = bib.replace('%R,','')
                    data=bibcodes.strip(", ")
                    print data
                    bibs.write(data+'\n') #writing bibcode
            except IndexError:
                pass
                
bibs.close()
if os.stat(bibfile)[6]==0:
    print 'no bib codes to add'
else:
    print 'finished creating output files'