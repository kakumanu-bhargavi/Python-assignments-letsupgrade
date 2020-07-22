#!/usr/bin/env python
# coding: utf-8

# In[1]:

1.sum1 of n natural numbers using while loop

num = int(input("enter a value of n:"))
hold = num
sum1 = 0
if num <= 0:
    print("Enter a positive number")
else:
    while num > 0:
        sum1 = sum1 + num
        num = num - 1;
    print("the sum of",hold, "natural num is:", sum1)


# In[18]:
2.find a number is prime number or not

num = int(input("Enter a number"))
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")


# In[ ]:




