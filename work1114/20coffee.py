# 문제
money = 0 #입금한 돈
sel = 1 #기능
cho = 0 #수량

money = int(input('요금>>>>>'))

while True:
    print('\n----- 커피 -----')
    print(f'현재 남은 금액: {money}원')
    print('1. 커피(300), 2.코코아(350), 3.반환, 4.충전, 5.종료')
    sel = int(input('기능선택>>>>>'))
    if sel == 1:
        cho = int(input('개수선택>>>>>'))
        if money>=300:
            charge = money-(300*cho)
            if charge >= 0:
                print(f'{sel} 커피를 {cho}개 구매 완료하였습니다. 사용금액: {300*cho} 거스름돈: {charge}원')
                money = charge
                continue
            else:
                print(f'구매하신 {cho}개 만큼의 커피를 구매하실수 없으니 남은금액을 확인하세요')
                continue
        else:
            print('커피를 구매하실수 없습니다. 금액확인후 주문하세요')
            continue
    elif sel == 2:
        cho = int(input('개수선택>>>>>'))
        if money>=350:
            charge = money-(350*cho)
            if charge >= 0:
                print(f'{sel} 커피를 {cho}개 구매 완료하였습니다. 사용금액: {350*cho} 거스름돈: {charge}원')
                money = charge
                continue
            else:
                print(f'구매하신 {cho}개 만큼의 코코아를 구매하실수 없으니 남은금액을 확인하세요')
                continue
        else:
            print('코코아를 구매 하실수 없습니다. 금액확인후 주문하세요.')
            continue
    elif sel == 3:
        print(f'현재 남은 금액은 {money}원 입니다.')
        continue
    elif sel == 4:
        full = int(input('충전금액>>>>>'))
        money += full
        print(f'{full}원 만큼 충전 되셨습니다. 현재금액={money}')
        continue
    elif sel == 5:
        print('감사합니다. 또 주문해주세요')
        break
