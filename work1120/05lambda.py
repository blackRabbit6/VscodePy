import time

# print('람다식 결과= ',(lambda x: x*3+2)(6))
# print('람다식 결과= ',(lambda a,b: a+b)(12,7))
# (lambda 키워드 매개인자x: 수식)()

def mybook(a,b):
    if a%2 == 0:
        return a
    else:
        return b

print('일반식 결과= ', mybook(36,79))
# (lambda 키워드 매개인자a,b: true if 조건 else faise)(36,79)
print('람다식 결과= ',(lambda a,b: a if a%2 == 0 else b))

print()