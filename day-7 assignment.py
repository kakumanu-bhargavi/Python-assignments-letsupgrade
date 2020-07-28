#!/usr/bin/env python
# coding: utf-8

# In[13]:


port1={21:"FTP",22:"SSH",23:"telnet",80:"http"}
port2=dict([(value,key)for key,value in port1.items()])
print("port2=",port2)


# In[20]:


sum1=[(1,2),(3,4),(5,6)]
print("the original tuple is:" +str(sum1))
res=[x+y for (x,y)in sum1]
print("the sum of tuple is:" +str(res))


# In[ ]:




