#08listcolor.py
color=['yellow','red','blue','purple','orange']

# 문자열로 구성 리스트
# 리스트데이터에 검색 in
print(color)
print('- '*50)
while True:
    print()
    my = input('검색컬러>>>')
    if my in color:
        print('결과 ', my in color)
    elif my=='q' or my=='quit' or my == 'exit':
        print('컬러 검색 프로그램 종료')
        break
    else:
        print('결과 ', my in color)

print('\n프로그램 종료')