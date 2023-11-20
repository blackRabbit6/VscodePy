import time
import csv
import codecs 

path='C:/Users/LG/OneDrive/바탕 화면/python/work1117/data/zktest.csv'
csv = codecs.open(path, 'r', encoding='utf-8') 
# csv = open(path, 'r', encoding='euc-kr') 
data = csv.read()
print(data)
print(path, '파일열기 성공했습니다')




print()
print()