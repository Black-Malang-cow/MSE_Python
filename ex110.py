#!/usr/bin/env python
# coding: utf-8

# In[4]:


if True :   #맨 위쪽의 if가 항상 참이기 때문에 7번째 줄의 else는 실행이 되지 않는다.
    if False: #여기의 if는 항상 거짓이기때문에 3,4번째 줄이 실행이 되지 않는다.
        print("1")
        print("2")
    else:      #2번째 줄if가 항상 거짓이기때문에 6번째 줄이 실행이 된다
        print("3")
else :     #맨위의 if 가 항상 참 이기때문에 실행이 되지 않는다.
    print("4")
print("5")  #어떠한 if문에도 속해있지 않으므로 그냥 실행이 된다. #11번


# In[ ]:




