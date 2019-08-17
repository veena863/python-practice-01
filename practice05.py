#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Introduction to dictionary datatype
"""Adictionary datatype in python is a collection of key-value pairs
each key is connected with a value
Dictionary is a mutable datatype--->we can add,modify and delete the values
we are using {}"""

alien_0={'colour':'green','point':5}
print(alien_0)
print(alien_0['colour'])
print(alien_0['point'])


# In[7]:


#How to intialize a empty dictionary

alien_1={}
alien_1['colour']='yellow'
alien_1['points']=10
alien_1['score']=50
print(alien_1)
print(f"the alien is in {alien_1['colour']}")
alien_1['colour']='blue'
print(f"the alien is now in {alien_1['colour']}")

#using get to access the values
get() method will be to print out the message.


# In[8]:


#Introduction to Tuple_data type
"""Why tuple is needed?
if we want a list of items that cannot change, then we want to create a rectangle that should always be an fixed"""

Area_Rect=(10,20,30)
print(Area_Rect[0])
print(Area_Rect[1])


# In[9]:


Area_Rect=(10,20,30)
Area_Rect[0]=40

# Here we get the error as
#'tuple' object does not support item replacment


# In[17]:


#Looping throuh an tuple by using for loop
Area_Rect=(10,20,30)
for Area in Area_Rect:
    print(Area)
#'Area' is a temparory variable
    


# In[19]:


#Writing over tuple
"""if we want to change the values in tuple then we use this concept without error
if we need ti change any of the item in tuple then we need to do it from scratch i.e from starting as shown below"""

Area_Rect=(10,20,30)
Area_Rect=(40,50,60)
print(Area_Rect)


# In[21]:


Area_Tri=(1,2,3)
print("original values:")
for x in Area_Tri:
    print(x)

Area_Tri=(4,5,6)
print("\n Modified Values:")
for x in Area_Tri:
    print(x)


# In[ ]:


#Styling Guide----->PEP8
#PEP---->Python enhancement Proposals
#1 line length---->should not exceed more than 80 words
#2 Maintaining blank lines
#3 Indentation----->4 spaces of lines


# In[23]:


#Introduction to if condition:

#1 if my car is bmw then i want to be in uppercase
#2 if not other car then i want it to be title case
cars=['audi','bmw','benz','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())


# In[32]:


#True or false of the statement:

#1
car='rangeover'
#car=='rangeover'
car.title()=='Rangeover'


# In[37]:


#Checking wheather a value is in list:

requested_toppings=['mushroom','corn','pineapple']
#'mushroom' in requested_toppings
#'mushroom' not in requested_toppings
'pepperoni' not in requested_toppings


# In[38]:


#Boolean Expressions:
#it declares true or false of the given condition
age=19
if age>=18:
    print('you are old enough to vote!')
else:
    print('sorry,you are too young to vote!')


# In[40]:


#Introduction to user inputs:
message=input("Tell me something and i will repeat it for you ")
print(message)


# In[41]:


age=input("how old are you? ")
print(age)


# In[ ]:




