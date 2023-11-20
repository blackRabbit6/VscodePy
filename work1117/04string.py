# mylist=[10,20,30,40,50,60,70]
# # print(mylist[시작=2:끝=5-1])
# print(mylist[2:5]) #[30, 40, 50]
# print(mylist[2:5:1]) #[30, 40, 50]
# print(mylist[::2]) #[10, 30, 50, 70]
# print(mylist[::-2]) #[70, 50, 30, 10]
# print('길이= ', len(mylist))
# # 에러 = print('길이 = ', mylist.len())

print('hello'.upper()) #대문자
print('HBI'.lower()) #소문자
print('Guido van Rossum1'.split()) #['Guido', 'van', 'Rossum1']
print('Guido van Rossum2'.split(' '))
print()
print('Apple,Banana,Orange'.split(',')) #['Apple', 'Banana', 'Orange']
print('Apple|Banana|Orange'.split('|')) #['Apple', 'Banana', 'Orange']

msg = 'appleABabws'
print(msg.count('a'))
print(msg.count('k'))

a,b,hap=4,25,0
hap= a+b
print('{}+{}={}'.format(a,b,hap))
print('{} python!!!'.format('hello'))
print('{0} python!!!'.format('hello'))
print('{0} {1}!!!'.format('hello','python'))
print()

msg='sundaymonday'
print(msg.find('h')) # -1(데이터 없을때)

ret =','.join(msg)
print(ret)
msg='  sundaymonday  '
print(msg+'hb')
print(msg.lstrip()+'hb')
print(msg.rstrip()+'hb')
print(msg.strip()+'hb')
print('ktlgsk'.replace('lg','LG폰사망'))

print()
print('- '*50)