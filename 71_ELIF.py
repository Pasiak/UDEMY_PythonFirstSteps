#!/usr/bin/env python
# coding: utf-8

# In[3]:


age = 27
isDrunk = False
isRestrictedArea = True 


# In[4]:


if age <18:
    print("you are too young to boy alcohol")
elif isDrunk:
    print("Are you drunk?")
elif isRestrictedArea:
    print("Restricted area")
else: 
    print("OK we can sell it to you")


# In[8]:


minLikes = 500
minShares = 100
likes = 600
shares = 1

if minLikes < likes and minShares > shares:
     print("Zbyt mało udostępnień")
elif minLikes > likes and minShares < shares:
    print("Zbyt mało lajków")
elif minLikes < likes and minShares < shares:
    print("obniżka cen")


# In[ ]:




