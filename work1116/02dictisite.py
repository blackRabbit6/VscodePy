#
mysite = dict() 
mysite['kakao'] = 'www.rain.com'
mysite['goole'] = 'www.snow.com'
mysite['naver'] = 'www.wind.com'

print(mysite.keys())
print()
print(mysite.values())
print()

try:
    print('열거형 enumerate(딕트값)')
    for i,j in enumerate(mysite):
        print(i,j,mysite[j])
        # print(j,mysite[j])
except Exception as ex:
    print('실행 중 에러: ',ex)

print()

# 딕트 기본출력
# for key in mysite:
#     print(key, ' ', mysite[key])

# print()
# for k,v in mysite.items():
#     print(k, ' ', v)

# print()
# for k in mysite.items():
#     print(k)  #튜플타입으로 출력 ( ) ('naver', 'www.네이버.com')

print()
print('- '*50)