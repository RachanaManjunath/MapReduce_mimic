#!/usr/bin/env python
# coding: utf-8

# ## **Data Cleaning Function**
# 
# In[ ]:


import re

def dataclean():
  #Remove digits
  with open('Pride_and_Prejudice.txt') as f:
    data = ''.join(i for i in f.read() if not i.isdigit())

  with open('Pride_and_Prejudice.txt', 'w') as f:
    f.write(data)
  #Remove special characters
  string = open('Pride_and_Prejudice.txt').read()
  new_str = re.sub(r"[^a-zA-Z\n]+", ' ', string)
  open('Pride_and_Prejudice.txt', 'w').write(new_str)
  #Convert uppercase to lowercase
  file = open('Pride_and_Prejudice.txt', 'rt')
  result = file.read().lower()
  file.close()

  out = open('Pride_and_Prejudice.txt','w')
  out.write(result)
  out.close()
  
#Verify clean text file
print(open('Pride_and_Prejudice.txt').read())

# ## **Data Split Function**
# In[126]:

def split():

  a_file = open("Pride_and_Prejudice.txt", "r")

  list_of_lists = []
  for line in a_file:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    list_of_lists.append(line_list)

  a_file.close()

#print(list_of_lists)

part1 = list_of_lists[0:5000] #first 5000 lines
part2 = list_of_lists[5000:]  #rest of the lines
print(part1)
print(part2)


# ## **Mapper Function**
# In[127]:

def mapperfunction(splitparts):
  out = []
  for line in splitparts:
      for word in line:
        out.append((word,1)) #append value 1 to each word
  return out


int_KV_1 = mapperfunction(part1)
int_KV_2 = mapperfunction(part2)


all_KV_pairs = int_KV_1 + int_KV_2 #add kyey-value pairs from part1 and part2
print(all_KV_pairs) #all the key value pairs
 
# In[128]:

def sortfunction(KV):
  
    KV.sort(key = lambda x: x[0]) #sort alphabetically

    return KV

sorted_KV = []
sorted_KV = sortfunction(all_KV_pairs)

print(sorted_KV) #sorted key value pairs


# ## **Partition Function**
# In[129]:

def partition(inp):

  alpha1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
  alpha2 = ['n','o','p','q','r','s','t','u','v','w','x','y','z']
  r1 = [ndx for ndx in inp if ndx[0][0][0] in alpha1] #has all key value pairs from a-m
  r2 = [ndx for ndx in inp if ndx[0][0][0] in alpha2] #has all key value pairs from n-z

  return r1, r2

atom = []
ntoz = []
atom,ntoz = partition(sorted_KV) #store the KV pairs in a-m and n-z respectively
print(atom)
print(ntoz)


# ## **Reducer Function**
# In[130]:

def reducer(x):
    
    finalresult =[]
    k = None
    word = None
    count = 1

    for z in x:
      word,v = z
      if k == word:        #if word exists in k, increase count. 
        count += 1
      else:
        if k:
          finalresult.append((k,count))  #if not, simply append the word with 1 to finalresult
        k = word
        count = 1
    return finalresult

#all KV pairs grouped by key, each key has value that represents total occurences in text
output1 = reducer(atom) 
output2 = reducer(ntoz)
print(output1) #verify
print(output2) #verify       

# ## **Main Function**
# In[131]:

def main(reducer_op1,reducer_op2):

  d ={}


  #output1 = reducer(atom) #call reducer function on sorted KV pairs a-m
  #output2 = reducer(ntoz) ##call reducer function on sorted KV pairs n-z
  Final_Result = output1 + output2 #combine
  print(Final_Result) #Final result

  d = dict(Final_Result) #store in dictionary

  df = pd.DataFrame(d.items(),columns = ['Word','Count']) #convert to data frame
  print(df)
  df.to_csv('Final_word_count.csv') #create csv file


main(output1,output2)
