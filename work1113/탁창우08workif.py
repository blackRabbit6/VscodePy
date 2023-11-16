a, b, c = 2, 7, 1

#if~elif~else
#if 안 if~elif elif안 if~elif~else 다시 
#낮은수 순 출력

if a>b:
    if a>c:
        if b>c:
            a,b = b,a
            a,c = c,a
            b,c = c,b
        elif c>b:
            a,b = b,a
            a,c = c,a
            b,c = b,c
elif b>c:
    if b>a:
        if c>a:
            a,b = a,b
            a,c = a,c
            b,c = c,b
        elif a>c:
            a,b = a,b
            a,c = c,a
            b,c = c,b
elif c>a:
    if c>b:
        if a>b:
            a,c = a,c
            b,c = b,c
            a,b = b,a
        elif b>a:
            a,c = a,c
            b,c = b,c
            a,b = a,b
print(a,b,c)

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print(a,b,c)