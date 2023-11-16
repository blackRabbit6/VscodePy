# 문서파일명기술
# 작성: 자신 이름

a=19
b=3
mok=a/b
ret=a//b  #몫(정수값만) 표시


print('mok = ', mok)
print('ret = ', ret)
print('-'*100)
print('몫 = %f' %mok) # %d(정수) %s(문자) %f(실수-소수6짜리까지 나옴)
print('몫 = %.2f' %mok) # %.(원하는 소수짜리 까지)f
print('몫 = ', round(mok, 2)) #round(값, 자릿수표현)

print()
# 내장함수 print() 모니터풀력, type() round()