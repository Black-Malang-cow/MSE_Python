#!/usr/bin/env python
# coding: utf-8

# In[3]:


date = ['09/05', '09/06', '09/07', '09/08', '09/09']   #10번
close_price = [10500, 10300, 10100, 10800, 11000]
print(dict(zip(date,close_price )))
#zip 을 통해 날짜하고 마감가격을 붙인다. 0번은 0번끼리 1번은 1번끼리 
#붙여지게 된다.
# 붙여진 것들에 dict를 이용하여 dict자료형으로 바꾸어 준다


# In[ ]:




