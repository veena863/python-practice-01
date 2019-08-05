#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""Introduction to for loop
looping through an entire list
without print we have to print each with index position"""

cricketers=['yuvi','dhoni','kholi']
for i in cricketers:
    print(i)
    

#the space before print in for loop is called as indentation i.e, 4 line of free space 


# In[32]:


#Example of for loop with the f-strings
cricketers=['yuvi','dhoni','kholi']
for i in cricketers:
    print(f"{i},that was a great trick!")
print(f"i cant wait to see you in next week,{i}")


#for last print statement it prints only once because above statement has come out of for loop and i is holding only variable in the list"""


# In[25]:


#making numerical list

#1  Range function

for x in range(1,5):
    print(x)
"""second position in the range is called as non inclusive or exclusive value because output prints from first position
to before last of second position"""


#2  list
numbers=list(range(1,6))
print(numbers)

#3 Even numbers

for x in range(2,11,2):
    print(x)
    
#Third position is the differnce in which we want to print the output


# In[28]:


# Statistical operations on a list

digits=list(range(1,11))
x=min(digits)
print(x)
y=max(digits)
print(y)
z=sum(digits)
print(z)


# In[47]:


#silicing of list: it is a sublist of list

players=['yuvi','dhoni','sachin','dravid','kholi']
print(players[0:5:2])


# In[ ]:




