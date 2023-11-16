a = 7
b = 3

hap,sub,gob,mok,nmg = 0,0,0,0,0
hap = a + b
sub = a - b
gob = a * b
mok = a / b
nmg = a % b
print(hap, sub, gob, mok, nmg)

print(a, '-', b, '=', sub) #,콤마기준으로 공백
print('%d-%d=%d' %(a,b,sub))
print('{}-{}={}'.format(a,b,sub))
print(f'{a}-{b}={sub}') #권장