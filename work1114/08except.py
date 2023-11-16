
su1, su2, hap, mok = 0,0,0,0
try:
    su1 = int(input('sul>>>>'))
    su2 = int(input('su2>>>>'))

    hap = su1+su2
    mok = su1/su2
except Exception as ex:
    pass
    print('에러이유 ', ex)

print()
print('합= ',hap)
print('몫= ', mok)
print()

print('영수증출력')
print('주차비대체')
print('안녕히 가세요')
print()

#08except문서