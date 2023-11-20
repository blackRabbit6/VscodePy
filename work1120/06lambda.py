import time

# print('람다식 결과= ',(lambda x: x*3+2)(6))
# print('람다식 결과= ',(lambda a,b: a+b)(12,7))
# (lambda 키워드 매개인자x: 수식)()
# (lambda 키워드 매개인자a,b: true if 조건 else faise)(36,79)
# print('람다식 결과= ',(lambda a,b: a if a%2 == 0 else b))
# 람다 조건식은 무조건 if else 만

a = list(range(1,11,1))
print(a)
print()
# 람다식을 이용해서 짝수출력
print('람다 = ', (lambda a: a%2==0)(36)) #True
print('람다 = ', list(map(lambda a: a%2==0,a))) 
print('람다 = ', list(filter(lambda a: a%2==0,a))) 




print()