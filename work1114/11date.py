import datetime
import time

print('aa')
time.sleep(0.2)

print('blue')
time.sleep(0.2)

print('cherry')
time.sleep(0.2)
print()

dt = datetime.datetime.now()
print(dt)
print(dt.strftime('현재날짜: %Y년-%m월-%d일'))
print(dt.strftime('현재시간: %H시 %M분 %S초'))
print()

import time
b = time.localtime()
print(b)
print(b.tm_year,'년',b.tm_mon,'월',b.tm_mday,'일')
print(b.tm_hour,'시',b.tm_min,'분',b.tm_sec,'초')
print()