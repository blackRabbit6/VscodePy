#07input.py
# 파이썬 모니터 출력 print() 자동라인개행
# 파이썬 키보드 입력변수 = input('안내문>>>')
# input()=결과는 문자열, 실수(정수) = int(input()) 쓰기
# 300이상 보너스 0.1
# 300미만 보너스 0.7
pay,bonus,total = 0,0,0

pay = int(input('급여>>>>'))
if pay>=300:
    bonus = pay*0.1
else:
    bonus = pay*0.7
total = pay + bonus
print(f'들어오는 금액은 {total}만원입니다.')

#파이썬 switch 제어 지원 X
#파이썬 연산처리에서 단항 지원 X
print()