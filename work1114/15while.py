#15while.py
# while 조건:
#     반복처리 

print('15while.py반복문 실습')
su,hap=0,0
while True:
    #10회  0~9까지 
    su += 1 # 파이썬 단항 1씩 증가, 1씩빼기 지원 X
    print(su, end='\t')
    hap += su
    if su==10:
        break
print('hap = ', hap)

# 아래처럼 출력
# 1 2 3 4 6 7 8 9 10
print()
