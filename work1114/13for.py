# 12for.py
# for 대표변수 in 범위 range():
# for 대표변수 in 범위 range(1,20,1):
#       1부터 20-1까지 1씩 올라감
#       3번째 1씩 증가일때 1생략가능
#     반복처리될 내용기술

su, hap = 0,0
for a in range(10):
    #10회 반복, 0~(10-1)까지
    print(a) #세로로 나옴
    print(a, end='') #가로정렬-붙어서 나옴
    print(a, end='\t') #가로정렬-띄어져서 나옴

print()
for b in range(1,11,1):
    #1에서 시작해서 11회 반복 1~(11-1)까지 출력
    print(b, end='\t')
print()
# 12for.py = 13for.py 구조동일(범위만다름)