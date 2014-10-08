# coding: utf-8

from datetime import datetime
import ast
import math

worddict = (open('rawWordDict.txt','r+')).read() #txt file that only has your dev key
cleanwords = worddict[18:-2]
shorter = ast.literal_eval(cleanwords)
timestamp = datetime.now().strftime("%Y_%m%d_%H%M")


cloudseeder = open('cloudseeder'+timestamp+'.txt', 'w')
num_list = []
for k in shorter:
    number = shorter[k]['total_occurences']
    num_list.append(number)    
    for i in range (0,number):
        cloudseeder.write(k+'\n')
cloudseeder.close()

#This section is very similar to above, but it exaggerates the weighting of terms.
nums = list(set(num_list))

def roundup(x):
    return int(math.ceil(x / 10.0)) * 10

rounded = roundup(nums[-1])
range_num = rounded / 3

cloudseederex = open('cloudseeder-exaggerated'+timestamp+'.txt', 'w')

for k in shorter:
    number = shorter[k]['total_occurences']
    if number < range_num:
        for i in range (0,number):
            cloudseederex.write(k+'\n')
    elif range_num <= number < (range_num*2):
        for i in range (0,number*2):
            cloudseederex.write(k+'\n')
    elif number >= (range_num*2):
        for i in range (0,number*3):
            cloudseederex.write(k+'\n')
cloudseederex.close()


print "Finished, check for cloudseeder and cloudseeder-exaggerated files."