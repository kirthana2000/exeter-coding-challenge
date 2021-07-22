#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import time
start= time.time()
dicfile = open("french_dictionary.csv","r")
#Retrieve all english and french words from csv and stroring it in dict{}
my_dic={}
for line in dicfile:
    currentline=line.rstrip("\n").split(',')
    my_dic[currentline[0]]=currentline[1]


# In[2]:


#%%time
frequency = {}
sorucefile = open( 't8.shakespeare.txt', 'r+' )
tempfile=open( 't8.shakespeare.translated.txt', 'w' )

#Fetch each line from sourcefile.
for line in sorucefile:
    #Fetch each word from line.
    for word in line.split(' '):
      #Check whether the word is in my_dict{} and not equal to new line.
      if word!='\n' and word in my_dic.keys():
          #Write corresponding french word in tempfile using dictionary keys.
          tempfile.write(my_dic[word]+" ")
          #check whether the word is in frequency{} and iterate it.
          if word in frequency:
            frequency[word]+=1
          #If not set the key value as "1".
          else:
            frequency[word]=1
      #If word not in my_dict{}, write the word. 
      else:
        tempfile.write(word+" ")

tempfile.close()


# In[3]:


from collections import OrderedDict
#Sort the frequency{} in ascending order.
occurence = OrderedDict(sorted(frequency.items()))


# In[4]:


csvwriter=open("frequency.csv","w")
freq=csv.writer(csvwriter)
freq.writerow(['English word','French word','Frequency'])

#write the frequency of each translated word in csv
for key in list(occurence.keys()):
    freq.writerow([key,my_dic[key],occurence[key]])
csvwriter.close()
end=time.time()


# In[5]:


get_ipython().system('pip install humanfriendly')


# In[6]:


import os, psutil
from humanfriendly import format_timespan
#calculate time taken and memory used
str1="Time to process: "+format_timespan(end-start)
str2="Memory used: "+str(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)+" MB"

with open("performance.txt","w") as per:
    per.write(str1+"\n"+str2)


# In[ ]:




