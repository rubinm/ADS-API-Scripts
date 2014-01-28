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
    if maxsecondletter == 0:
        howmanytimes=range(maxmodulus)
    else:
        howmanytimes=range(maxmodulus+1)
    j=1
    for i in howmanytimes:
        firstletter = standard_mapping[i]
        if i==(len(howmanytimes) - 1 ) and maxsecondletter!=0:
            letters = [firstletter+standard_mapping[k] for k in range(maxsecondletter)]
        else:
            letters = [firstletter+standard_mapping[k] for k in range(26)]
        for l in letters:
            try:
                out = l+'('+affiliations[j].strip()+')'
                outs.append(out)
                j=j+1
            except IndexError:
                pass
    return outs

#/end Rahul's script

#this is where you put in new typos

           #"bad":"good",
typos  =   {"  ":" ",
            ",,":",",
            ",)":")",
            "..":".",}

def cleanup(stuff):
    for k, v in typos.iteritems():
        stuff = stuff.replace(k, v)
    return stuff

#/end typo function

#This creates and writes a file called "metadata_updates(timestamp).txt" that will list all author/affiliation updates marked on checkaffil.csv

timestamp = datetime.now().strftime("_%Y_%m%d_%H%M")

metadata_updates = open('cfametadata_updates'+timestamp+'.txt', 'w')

with open('checkaffil.csv', 'rb') as f:
    reader = csv.reader(f)
    print "bibcodes that are being updated"
    for row in reader:
        #print row
        if '%Rc' in row:
            row.pop(2)
            bib = ('; ').join(row)
            bibcodes = bib.replace('%Rc;','%R')
            data=bibcodes.strip("; ")
            print data
            metadata_updates.write(data+'\n')  
            
        elif '%Ac' in row or '%Ax' in row:
            auth = ('; ').join(row)
            authors = auth.replace('%Ac;','*%A').replace('%Ax;','%A')
            data=authors.strip("; ")
            cleaned = cleanup(data) #removes common errors as writen in the above cleanup function
            metadata_updates.write(cleaned+'\n')  

        elif '%Fc' in row or '%Fx' in row:
            h=alphabets2(row) #uses Rahul's above function
            h=[e for e in h if e[-2:]!='()'] #more code from Rahul!
            affil = (', ').join(h)
            data = (row[0]+" "+affil).replace('%Fc','*%F').replace('%Fx','%F')
            cleaned = cleanup(data) #removes common errors as writen in the above cleanup function
            metadata_updates.write(cleaned+'\n')  
            metadata_updates.write('\n')

metadata_updates.close()

#This creates and writes a file called "cfabib(timestamp).txt" that will list all bibcodes marked on checkaffil.csv

filename = 'cfabib_updates'+timestamp+'.txt'
cfabib_updates = open(filename, 'w')

with open('checkaffil.csv', 'rb') as f:
    reader = csv.reader(f)
    print "\nbibcodes to add to CfA Bib"
    for row in reader:
        
        if '%Rc' in row or '%R' in row:
            try:
                if 'x' in row[2]:
                    row.pop(2)
                    bib = (', ').join(row)
                    bibcodes = bib.replace('%Rc,','').replace('%R,','')
                    data=bibcodes.strip(", ")
                    print data
                    cfabib_updates.write(data+'\n') #writing bibcode
            except IndexError:
                pass

cfabib_updates.close()

if os.stat(filename)[6]==0:
   print 'no bib codes to add'
else:
   print 'Finished creating output files - Yay!'