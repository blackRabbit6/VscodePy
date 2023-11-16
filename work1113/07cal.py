#07cal.py 출력연습
kor,eng,hap,avg = 0,0,0,0
ret = ''    #시험결과
grade ='F'  #학점 

kor = 65
eng = 60
hap = kor + eng
avg = hap / 2

if avg >= 70 :
    ret = '축합격'
else:
    ret = '재시험'

#grade변수에 학점 100~90 A, 89~80 B, 79~70 C, 69~60 D,  0~59 F
#if~elif~else
if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'
else:
    grade = 'F'


print('총점:' , hap)
print('평균:' , avg)
print('학점:' , grade)
print('결과:' , ret)
print('-' * 100)
print() 
