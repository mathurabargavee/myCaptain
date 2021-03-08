#!/usr/bin/env python
# coding: utf-8

# In[3]:


list=[]
n=int(input("Enter number of elements:"))
print("Enter the elements:")
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print("The positive elements in the list are:")
for i in range(0,n):
    if list[i]>=0:
        print(list[i],end =" ")
        


# In[ ]:




