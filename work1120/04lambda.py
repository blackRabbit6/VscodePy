import time

def mytest(x):
    su = x*3+2
    return su

data = mytest(6)
print('일반식',data)

print('람다식 결과= ',(lambda x: x*3+2)(6))
#lambda 키워드 매개인자x: 수식

print()

def myadd(a,b):
    hap = a+b
    return hap

time.sleep(1)
value = myadd(12,7)
print('일반식 걀과= ',value)
print('람다: ',(lambda a,b: a+b)(12,7))