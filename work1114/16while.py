# 16while.py
print('16while.py반복문 실습')
su=0
while True:
    su += 1 
    print(su, end='\t')
    if su%5 == 0:# 1줄에 5개 씩 출력
        print()
    if su == 30:
        break
# 강종 ctrl c
print()
print('우리나라a')
print('다른나라b')
print('세계전체c')
print()