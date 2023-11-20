import time
import csv
import codecs 

#13filecsv.py문서 작성  지난주 금요일 work1117폴더  13filecsv.py
path='C:/Users/LG/OneDrive/바탕 화면/python/work1117/data/zktest.csv'
with codecs.open(path, 'w', encoding='utf-8') as fw:
    file=csv.writer(fw, delimiter=',')
    file.writerow(['id', 'name', 'price'])
    file.writerow(['100', '객체지향자바교재', '6400'])
    file.writerow(['200', '파이썬책마우스', '8500'])
    file.writerow(['300', '웹&앱관련eBook', '4600'])

time.sleep(0.3)
print(path, '파일저장 성공했습니다')

print()
print()