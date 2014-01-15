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
            out = l+'('+affiliations[j].strip()+')'
            outs.append(out)
            j=j+1
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

timestamp = datetime.now().strftime("%Y_%m_%d_%H%M")

metadata_updates = open('cfametadata_updates'+timestamp+'.txt', 'w')

with open('checkaffil.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        #print row
        if '%Rc' in row:
            row.pop(2)
            joined = ''
            bib = (', ').join(row)
            bibcodes = bib.replace('%Rc,','%R')
            data1=bibcodes.strip("; ")
            data=data1.strip(", ")
            print data
            metadata_updates.write(data+'\n')  
            
        elif '%Ac' in row:
            joined = ''
            auth = ('; ').join(row)
            authors = auth.replace('%Ac;','*%A')
            data1=authors.strip("; ")
            data=data1.strip(", ")
            cleaned = cleanup(data)
            print cleaned
            metadata_updates.write(cleaned+'\n')  

        elif '%Ax' in row: #marked Ax if the author field was not updated, but Louise wants in the file
            joined = ''
            auth = ('; ').join(row)
            authors = auth.replace('%Ax;','%A')
            data1=authors.strip("; ")
            data=data1.strip(", ")
            cleaned = cleanup(data)
            print cleaned
            metadata_updates.write(cleaned+'\n')  

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
            data = affil.replace('%Fc,','*%F')
            cleaned = cleanup(data)
            print cleaned
            metadata_updates.write(cleaned+'\n')  
            metadata_updates.write('\n')
            
        elif '%Fx' in row: #marked Fx if the affiliation field was not updated, but Louise wants in the file
            a=row
            #print a
            a.pop(0)
            outside=[]
            h=alphabets2(a) #uses Rahul's above function
            h=[e for e in h if e[-2:]!='()'] #more code from Rahul!
            data =  ['%Fx']+h
            joined = ''
            affil = (', ').join(data)
            data = affil.replace('%Fx,','%F')
            cleaned = cleanup(data)
            print cleaned
            metadata_updates.write(cleaned+'\n')  
            metadata_updates.write('\n')

metadata_updates.close()

#This creates and writes a file called "cfabib(timestamp).txt" that will list all bibcodes marked on checkaffil.csv

filename = 'cfabib_updates_'+timestamp+'.txt'
cfabib_updates = open(filename, 'w')

with open('checkaffil.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        
        if '%Rc' in row:
            try:
                if 'x' in row[2]:
                    row.pop(2)
                    bib = (', ').join(row)
                    bibcodes = bib.replace('%Rc,','')
                    data=bibcodes.strip(", ")
                    print data
                    cfabib_updates.write(data+'\n') #writing bibcode
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
                    cfabib_updates.write(data+'\n') #writing bibcode
            except IndexError:
                pass

cfabib_updates.close()

if os.stat(filename)[6]==0:
   print 'no bib codes to add'
else:
   print 'Finished creating output files - Yay!'