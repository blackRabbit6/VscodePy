import time
# f = open(1파일명,2모드w/r,3인코딩)
# with open(1파일명, 2'w', 3encoding='utf-8') as my:


# f = open(파일명,'wt/a/r',encoding='utf-8')
path  = 'C:/Users/LG/OneDrive/바탕 화면/python/work1117/data/test.txt'
f = open(path,'w',encoding='utf-8')
f.write('이순신\n')
f.write('lattee\n')
f.write('11-17-금\n')
f.write('3.14\n')
f.close()
time.sleep(0.3)
print(path, '파일저장 성공했습니다')

name  = 'C:/Users/LG/OneDrive/바탕 화면/python/work1117/data/sample.txt'
with open(name, 'w', encoding='utf-8') as my:
    my.write('카카오톡\n')
    my.write('카카오맵\n')
    my.write('카뱅크\n')
    my.write('1200\n')
    my.close()
time.sleep(0.3)
print(name, '파일저장 성공했습니다')    







print()
print()