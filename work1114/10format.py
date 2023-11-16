su = 7891
title = 'today is tuesday'

print(su)
print(title)
print()
print('{}'.format(su)) #숫자이지만 기본맞춤은 왼쪽
print('|{:>10}|'.format(su)) # 오른쪽 맟춤 권장 {}안에 :, (오른쪽,왼쪽,중앙 셋중하나), 자리수
print('|{:<10}|'.format(su)) # 왼쪽
print('|{:^10}|'.format(su)) # 중앙
print()
print('|{:0>10,}|'.format(su))
print('|{:*>10,}|'.format(su))