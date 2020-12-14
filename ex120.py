#!/usr/bin/env python
# coding: utf-8

# In[4]:


fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"} #12번
user = input("좋아하는 과일은?") #사용자로부터 입력을 받음
if user in fruit.values(): #과일은 키 값이 아닌 values 값이므로 values에 대해
                         #프로그래밍을 짜야한다.
    print("정답입니다.")# if문 참이면 정담입니다를 출력
else:
    print("오답입니다.") #거짓이면 오답입니다를 출력


# In[ ]:




