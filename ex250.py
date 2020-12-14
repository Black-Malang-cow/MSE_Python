#!/usr/bin/env python
# coding: utf-8

# In[8]:


#range 증가량은 정수만 가능    #25번

import numpy    #numpy모듈을 들여온다 
                 #증가량이 실수도 가능하게하기 위해서이다.   
for i in numpy.arange(0, 5, 0.1): #0 부터 5보다 작은수를 
                                   #0.1씩만큼 늘려서 나열한다
    print(i)


# In[ ]:




