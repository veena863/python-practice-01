#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Intoduction to while loop
current_number=1
while current_number<=5:
    print(current_number)
    current_number=current_number+1


# In[5]:


#Introduction to function:
#Functions are used for repetative process
def greet_users():
    print("Hello")
greet_users()


# In[ ]:


def greet_user(username)
#username is a parameter
"""Display a simple greeting to user loged in"""
print(f"Hello,{username.title()}!")
greet_user('Veena') #Function Calling--->Here Veena is a argument passing(we can change whenever we want)


# In[6]:


#More information about passing arguments
#1.Positional aruments
#2.Keyword arguments


# In[8]:


#1.Positional arguments:
def describe_pet(animal_type,pet_name):
    print(f"\n I have a {animal_type}")
    print(f"my{animal_type}'s name is {pet_name.title()}")
describe_pet('husky','bruno')
#This is apositional arguments(i.e) the position changes then the information will be changed so we have to give argumnets in exact position


# In[10]:


#2 Keyword arguments
describe_pet(pet_name='bruno',animal_type='husky')
#pet_name is keyword


# In[ ]:




