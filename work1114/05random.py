import math

print(19/6) #3.1666666666666665
print(19//6) #3
print(7%4) #3
print()
print('-'*100)

print(5*2) #사칙연산
print(5**2) #제곱
print(5**3) #3제곱
print()
print('-'*100)

#math수학관련함수 결과값 실수
# power() ===> pow()
print(math.sqrt(25)) 
print(math.sqrt(81))
print(math.pow(5,2)) #25.0
print(math.pow(9,2)) #81.0
print(5**2) #25
print(9**2) #81
print()
print('-'*100)
#내장함수 print()모니터출력, type(), round()
#수학함수 math.pow() math.sqrt()
#변환함수 int(),str(),float(),bin(2진수),oct(8진수),hex(10진수)
#난수발생 import random     정수형 randint(1,45)
import random
print('실수난수 ',random.random())
print('정수난수 ',random.randint(1,45))

print()