#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1=[1,2,3,4,5,6,7,8]
list2=['a','b','c','d','e']
result={}
for key in list2:
    for values in list1:
        result[key]=values
        list1.remove(values)
        break
print(str(result))


# In[ ]:




