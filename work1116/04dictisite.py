#
mysite = {} 
mysite['rain'] = 'www.rain.com' #딕트신규등록
mysite['snow'] = 'www.snow.com' #딕트신규등록
mysite['wind'] = 'www.wind.com' #딕트신규등록
mysite['rain'] = 'www.hbihong.com'  #딕트 동일한 key rain

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

print()
print('- '*50)