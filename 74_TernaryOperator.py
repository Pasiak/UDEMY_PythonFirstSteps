#!/usr/bin/env python
# coding: utf-8

# In[1]:


itRains = True


# In[2]:


if itRains:
    print("We stay at home")
else:
    print("We go out")


# In[3]:


print("We stay at home" if itRains else "We go out")


# In[4]:


#LAB


# In[12]:


musclePain  = False
fever = False
weakness = True
isMan =True


# In[13]:


print("suspicion of influenza" if musclePain and fever and weakness else "The flu is unlikely")


# In[14]:


if musclePain and fever and weakness:
    print("suspicion of influenza")
elif weakness and (not fever or musclePain):
    print("Just take a rest!")
else:
    print("you may be cold")


# In[ ]:




