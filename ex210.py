#!/usr/bin/env python
# coding: utf-8

# In[7]:


def message1(): #함수를 정의 함   21번
    print("A")

def message2():  #함수를 정의 함
    print("B")

def message3(): 
    for i in range (3) : #3번을 반복한다  0,1,2 가 바인딩 되므로
        message2() 
        print("C")
        #for 루프에 같혀있으므로 3번을 반복하고 빠져나갈 것이다.
    message1() #for루프와 상관이 없으므로 위에서 for루프를 
               #다 돌고 나와서 출력이 될것이다

message3()  


# In[ ]:




