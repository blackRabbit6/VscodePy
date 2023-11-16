#11split.py

my = [ 'first.c', 'info.h', 'define.h', 'test.py', 'hong.h']
# 파일명 확장로 분리  split()사용
# 문제1 결과  ['first', 'c'] ['info', 'h'] ['define', 'h'] ['test', 'py']  ['hong', 'h'] 
# 문제2 결과 'h' 데이터만 출력 if~~~~
ret = ''
for item in my:
    ret = item.split('.')
    #print(ret , end =' ')
    if ret[1]=='h' or ret[1]=='c':
        #print(item)
        print(ret , end =' ')













print()
print('-' * 100)