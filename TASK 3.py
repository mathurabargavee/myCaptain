#!/usr/bin/env python
# coding: utf-8

# In[6]:


n= int(input("Enter n value "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if n<= 0:
   print("Please enter a positive integer")
elif n== 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1


# In[ ]:




