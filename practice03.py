#!/usr/bin/env python
# coding: utf-8

# In[5]:


#How to change,add,deleting elements in a list

fruits=['Apple','mango','banana','gauava']
print(fruits)

#1changing elements in list

fruits[1]='pea'
print(fruits)


# In[2]:


#2 Adding/append the element in the list
fruits=['Apple','manga','banana','gauava']
print(fruits)
fruits.append('pineapple')
print(fruits)


# In[3]:


"""above we can observe that the added element is placed at the last of the list
if we want to place at any particular position then we need to define with a index position as below"""
fruits=['Apple','manga','banana','gauava']
print(fruits)
fruits.insert(2,'pineapple')
print(fruits)


# In[4]:


#Dymanic creation of empty list

friends=[]
print(friends)
friends.append('satya')
friends.append('teja')
friends.append('Anu')
friends.append('navee')
friends.insert(1,'harry')
print(friends)


# In[10]:


#3 deleting elements from list

#there are two differnt ments to delete the element from list

#a

icecreames=['chocalate','butterscotch','vanilla','tuttyfruity']
print(icecreames)
del icecreames[2]
print(icecreames)


#b

icecreames=['chocalate','butterscotch','vanilla','tuttyfruity']
icecreames.pop()
# the above syntax will delete the last element in the list
print(icecreames)
#inorder to delete the particular element in the list below has to be followed
icecreames.pop(1)
print(icecreames)

"""delete will delete the items permanently
whereas pop() will not delete its permeanently from memory
in popup items will be stored separately in another variable declared"""



# In[14]:


#4 how to sort a list?

veg=['carrot','beans','cabbage','bitterguard']
veg.sort()
print(veg)
veg.reverse()
print(veg)

veg=['carrot','beans','cabbage','bitterguard']
veg.reverse()
print(veg)


# In[15]:


#5 how to count the no. of elements in a list?
veg=['carrot','beans','cabbage','bitterguard']
print(len(veg))


# In[ ]:




