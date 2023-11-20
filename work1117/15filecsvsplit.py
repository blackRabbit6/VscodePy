import time
import csv
import codecs


path='C:/Users/LG/OneDrive/바탕 화면/python/work1117/data/zktest.csv'
csv = codecs.open(path, 'r', encoding='utf-8').read()

data = []
rows = csv.split('\r\n')
for row in rows:
    if row==' ':
        continue
    cells = row.split(',')
    data.append(cells)

print(data)
print()
for cell in data:
    print(cell[0],cell[1],cell[2])

print(path, '파일열기 성공했습니다')
print()
print()