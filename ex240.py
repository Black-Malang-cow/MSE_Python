#!/usr/bin/env python
# coding: utf-8

# In[8]:


def 함수0(num) : #24번
    return num * 2 #함수 1에서 받은 값에 2를 곱한다.

def 함수1(num) :
    return 함수0(num + 2)#함수2에서 받은num에 2를 더한 후 함수0 
                           #을 호출한면서 함수 0에 2를 더한 num값을 넣는다


def 함수2(num) : 
    num = num + 10 #num 에 10을 더한다
    return 함수1(num) #10을 더한 num 을 함수1을 호출한면서 함수 1에 넣는다

c = 함수2(2)   #함수2 에 2를 집어넣는다
print(c)


# In[ ]:




