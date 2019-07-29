#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Numbers
#1 Integers: Any plane digit is a integer
x=2;y=3;z=4
print(x,y,z)


#Advanced approach of assignment operator is

x,y,z=2,3,4
print(x,y,z)


# In[12]:


#2 Float:a number with a decimal number 
x=1.2
y=2.2
print(x+y)


# In[15]:


#3 Constant:variable whose is constant throughtout the program
#Constant is variable is declared in Capital letters
MAX_CONN=100
print(MAX_CONN)


# In[26]:


#Introduction to collection data types
#1 List : List is a mutable datatype which means we can modify the datatype
#List is defined in[]
fruits=['apple','mango','banana','orange']
print(fruits)
print(fruits[1].title())
fruits[1]='pineapple'#to change the value of certain we can refer the index
print(fruits[1].upper())

