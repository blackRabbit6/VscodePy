# 파이썬 피클 import pickle
# 파이썬 피클 pickle.dump()  저장
# 파이썬 피클 pickle.load()  열기

import pickle
import time

color = ['blue', '블루베리', '@#^*$&', 789, '오렌지']
path ='C:/Users/LG/OneDrive/바탕 화면/python/work1117/data/colors.pkl'
f = open(path, 'wb')
pickle.dump(color,f)
time.sleep(0.3)
print(path, '피클저장성공했습니다')







print()
print()
