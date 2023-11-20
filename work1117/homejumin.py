# import time #time= 현재시간
import datetime #현재 날짜 년도 등

jumin = '891027-1072638'
ju1 = '891027'
ju2 = '1072638'

# 문제1  성별추출 1/3남자  2/4여자
if(int(jumin[7])==1 or int(jumin[7])==3):
    print('남성')
elif(int(jumin[7])==2 or int(jumin[7])==4):
    print('여성')
else:
    print('주민등록 뒷자리에 맞지 않음')
# 문제2  고객의생일 10월27일 생일을 축하합니다
print('고객의 생일'+ju1[2:4]+'월'+ju1[4:6]+'일')
# 문제3  891027-1******
print(jumin.replace(jumin[8:],'*'*len(jumin[8:])))
# 문제4  import  time/datetime이용해서 나이 구하기 
#        2023-(2000+05)=나이     jumin = '051027-1072638'
#        2023-(1900+89)=나이     jumin = '891027-1072638'
now = datetime.datetime.now()
current = now.year
cen = 0
if(int(jumin[0:2])>=00 and int(jumin[0:2])<=23):
    cen = 2000
else:
    cen = 1900

age = current-(cen+int(jumin[0:2]))
print(f'현재 나이는 {age}세 입니다. jumin = {jumin}')
# 문제5 jumin 문자열 총길이 6 - 7
#       6자릿수가 아니거나 7자릿수가 아니면  주번 기입 잘못되었습니다
if(len(jumin[0:6])!=6 or len(jumin[7:])!=7):
    if(len(jumin[0:6])!=6):
        print('주민번호 앞자리 기입 잘못')
    else:
        print('주민번호 뒷자리 기입 잘못')
elif(len(jumin[0:6])!=6 and len(jumin[7:])!=7):
    print('주민번호 앞뒷자리 전부 다 기입 잘못')
else:
    print(f'주민번호 입력 완료, jumin = {jumin}')