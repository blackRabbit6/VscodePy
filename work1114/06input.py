#06input.py

name = input('name>>>')
age = int(input('age>>>'))
# 형변환
# input만쓰면 에러남 왜냐하면 age는 숫자인데, 그냥 쓰면 문자열로 이해하기때문
# 그렇기 때문에 input을 int로 묶어줘야 수로 인식함

print(f'이름={name}')
print(f'나이={age}')

#나이 60이상 시니어대상
#30~59사이 중장년대상
#1~15 어린이,초등학생
#16~29 청소년,청년
if age>=60:
    print('시니어대상')
elif age>=30:
    print('중장년대상')
elif age>=16:
    print('청소년, 청년대상')
else:
    print('어린이, 초등학생 대상')
print()