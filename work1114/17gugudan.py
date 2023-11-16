# 17gugudan.py

dan = 1
# 첫번째 키보드입력
# dan = input('원하는 단 입력>>>') 문자열 결과가 되기에 안됨
# 두번째 형변환
# 세번째 키보드입력시 문자 입력 except 처리
try:
    dan = int(input('원하는 단 입력>>>'))
except Exception as ex:
    pass
    print('다시 입력',ex)
#for문
for i in range(1,10,1):
    # print(dan,'*',i,'=',(dan*i))
    print(f'{dan} * {i} = {dan*i}')

