#!/usr/bin/ python
#encoding: UTF-8
import sys, codecs
import numpy as np

#opens file with the right encoding and read everything
filein = codecs.open(sys.argv[1], "r", "utf8") 
fullin = filein.read()
fulltext = fullin.lower() #make everything lower case
filein.close()

#this is the list of different characters
all_characters = list(set(fulltext))

# a list of charachters to remove from the all_characters list
to_remove = [' ', ',', '_', '.','(', ')', '#','"','[',']','\n', '\r', u'\x0c',u'\u011d', u'\u2014', u'\u016d', u'\u0109', u'\u2123']

for undesired in to_remove:
    try:
        all_characters.remove(undesired) #if undesired is not in the list, remove fails
    except:
        pass

#count the number of times in the text
frequencies = []
for valid in all_characters:
    n_times = 1.0 * fulltext.count(valid)
    frequencies.append(n_times)

#make a final list of frequencies and charachters
n_total = sum(frequencies)
final_list = []
rango=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
 
for item  in frecuencies:
    final_list.append(item)

#sort it
final_list.sort()
final_list.reverse()

vector = np.zeroes(20)
for i in range(20):
    vector[i]=vector[i]+final_list[i]

x=[]

for item in rango:
    np.log(item,a)                                    
    x.append(a) 
    
y=[]

for item in vector:
    np.log(item,b)
    y.append(b)
      
m= np.polyfit(x,y,1) 

#write it to a file

fileout = codecs.open("coeficientede"+sys.argv[1], "w", "utf8") 
fileout.write("coeficiente: %f\n"%(m[0]))
