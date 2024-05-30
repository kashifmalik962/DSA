#!/usr/bin/env python
# coding: utf-8

# In[1]:


stock_price = []
with open('stock_price.csv','r') as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_price.append([day,price])


# In[2]:


stock_price


# In[3]:


for i in stock_price:
    if i[0] == '08-Mar':
        print(i[1])


# In[8]:


stock_price = {}
with open('stock_price.csv','r') as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_price[day]=price


# In[9]:


stock_price


# In[11]:


stock_price['09-Mar']


# In[ ]:





# In[13]:


def get_hash(key):
    h = 0
    for char in key:
        h+=ord(char)
    return h % 10


# In[19]:


get_hash('march 7')


# In[89]:


class Hashtable:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]
        
    def get_hash(self,key):
        h = 0
        for char in key:
            h+=ord(char)
        return h % self.max
    
    def add(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def get(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def delete(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
        print(self.arr)


# In[90]:


ob = Hashtable()


# In[91]:


ob.get_hash('march 6')


# In[92]:


ob.add('march 6',310)


# In[93]:


ob.get('march 6')


# In[94]:


ob.delete('march 6')


# In[ ]:




