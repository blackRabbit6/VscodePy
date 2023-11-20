
species = ("Adelie", "Chinstrap", "Gentoo")  #tuple튜플, 추가 수정 하려면 list 화 --> 튜플화
penguin_means = {
    'Bill Depth': (18.35, 18.43, 14.98),
    'Bill Length': (38.79, 48.83, 47.50),
    'Flipper Length': (189.95, 195.82, 217.19),
}


score_dict = {
    '김자바' : [90,80],
    '이합격' : [50,77],
    '박이썬' : [63,67],
    '고길동' : [82,34]
}
# 함수 할때 
# def myTotal(x,y):
#   total = x+y
#   return myTotal 로 쓰지말고 바로 def 하고 다음에 바로 return x+y쓰는게 편함
def myTotal(x,y):
    return x+y
    
try:
    for i,j in enumerate(score_dict):
        total = myTotal(score_dict[j][0],score_dict[j][1]) 
        #여기서도 total대신 myTotal로 해버리면 함수명이랑 같아
        #int 객체로 덮어쓰여져 에러가남 그렇기 때문에 이 안에서 변수명을 다르게 쓰기
        print(i,j,score_dict[j][0],score_dict[j][1], 'total: ',total)
except Exception as ex:
    print('에러: ', ex)


print('\n총합계까지 출력')
tot = 0
for i, (key,data) in enumerate(score_dict.items()):
    tot += score_dict[key][a]
    print(i,key,data[0],data[1],'total: ', tot)
    tot = 0 #반드시 초기화작업
#해결준비작업
#0 김자바 90 80
#1 이합격 50 77
#2 박이썬 63 67
#3 고길동 82 34

#해결1 딕터 출력 enumerate()
#해결2 알고리즘처럼 중첩for 반복문 사용, if사용X, 변수 초기화
#해결3 함수 def myTotal(딕트값):

#0 김자바 90 80 total: 170
#1 이합격 50 77 total: 127
#2 박이썬 63 67 total: 130
#3 고길동 82 34 total: 118