import time
import sys #System.exit(1)역할, sys.exit() 프로그램 종료

menu = {}
while True:
    print()
    sel = int(input('1.등록 2.출력 3.수정 4.삭제 5.검색 9.종료>>>>>'))
    if sel == 9:
        print('딕트crud 프로그램 종료합니다\n')
        sys.exit()

    if sel == 1:
        pass #등록 딕트
        name = input('메뉴 이름 입력>>>>')
        price = int(input('메뉴 가격 입력>>>>'))
        menu[name] = price
        # menu['kim'] = 3400
        # menu['lee'] = 7800
    elif sel ==2:
        print('-----메뉴-----')
        # for i,(j,data) in enumerate(menu.items()):
        #   print(i,j,data)
        for i,j in enumerate(menu):
            print(i,j,menu[j])
    elif sel ==3:
        # 키값 변경 =pop()메서드 사용
        pass
        name = input('수정 메뉴 입력>>>>')
        if name in menu:
            value = menu.pop(name)
            change = input('변경할 메뉴명>>>>')
            menu[change] =value
            print(f'{name}이 {change}으로 변경되었습니다.')
        else:
            print('존재하는 이름이니 다시 확인하세요')
            continue
    elif sel ==4:
        pass
        name = input('삭제 메뉴 입력>>>>')
        # 삭제 = del
        if name in menu:
            del menu[name]
            print(f'상품명 {name}을 삭제 하였습니다.')
        else:
            print('제품이 존재하지 않으니 다시 확인하세요')
            continue
    elif sel ==5:
        pass
        name = input('검색 메뉴 입력>>>>')
        if name in menu:
            print(f'메뉴명: {name} 가격: {menu[name]}')
            #가격에 price 넣으니 처음 한게 저장이 되어버림 이때는 price= menu[name]으로 바꾸면 잘 나옴
        else:
            print('잘못 입력함')
            continue
    else:
        print('다시 입력하세요')
        continue