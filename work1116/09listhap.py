data=[
    [7,6,3,4,12], # 첫항목 = kor 점수
    [2,9,4,5,6] # 두번째 = eng 점수
]

# 문제 첫 번째 합계=32 평균=6.4
print('1번')
for i in range(5):
    print(data[0][i],end =' ')
print() #줄바꿈

total = sum(data[0])
print('합계: ',total)
avg = total/len(data[0])
print('평균: ',avg)

# 문제 두 번째 합계=26 평균=5.2
print('2번')
for j in range(5):
    print(data[1][j], end=' ')
print()

total1 = sum(data[1])
print('합계: ',total1)
avg1 = total1/len(data[1])
print('평균: ',avg1)