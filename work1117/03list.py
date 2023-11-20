# mylist[10,20,30,40,50,60,70]
melist=[50,60,70,90]
print(melist[1]) #60
print(melist[-1]) #90
print(melist[1:]) #60~끝까지
print(melist[:2]) #시작부터 2번앞까지
print(melist[2:7]) #2~7앞가지 갯수부족:에러없음
print()
print('- '*50)

# js,java, sql 문자추출 substring(),substr()
# 파이썬에서 [시작:끝-1] 추출
# 02list.py문서 03list.py문서 거의 동일

mylist=[10,20,30,40,50,60,70]
# print(mylist[시작=2:끝=5-1])
print(mylist[2:5]) #[30, 40, 50]
print(mylist[2:5:1]) #[30, 40, 50]
print(mylist[::2]) #[10, 30, 50, 70]
print(mylist[::-2]) #[70, 50, 30, 10]
print('길이= ', len(mylist))
print()
print('- '*50)