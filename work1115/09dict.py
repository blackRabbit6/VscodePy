# dict { k:v } 
# pos = { '제주':37.97485, '독도':127.62342, '시청':35.17485}
# print(pos)

pos = { '제주':37.97485 }
pos['홍대'] = 123.7890
pos['강릉'] = 45.1234
print(pos)
# 딕트에서 지원안되는 함수  append(), insert(), add() 

if pos.get('홍익대')==None:
    print('홍익대 key데이터가 없습니다 ')
else:
    print('수정,삭제,조회 작업가능합니다')















print()
print('- ' * 50)