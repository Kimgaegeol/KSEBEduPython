import random

drinks = ["위스키", "와인", "소주", "고량주"]
foods = ["초콜릿", "치즈", "삼겹살", "양꼬치"]
price = [50000, 30000, 5000, 20000]
total_price = 0

drinks.append("사케")
foods.append("광어")
price.append(10000)

amount = [0 for menu in drinks]

welcome_message = ""
choice = 0

def choiceMenuLogic(choice):
    try:
        global total_price
        choice = int(choice)
        if 1 <= choice and choice <= len(drinks):
            amount[choice - 1] += 1
            printMenu(choice)
            return
    except Exception as e:
        print("잘못된 입력입니다.")

def welcomeMessageLogic():
    global welcome_message
    welcome_message = "다음 술중에 고르세요.\n"
    for index, value in enumerate(drinks):
        welcome_message += str(index + 1) + ") " + value + "  "
    welcome_message += str(len(drinks) + 1) + ")  아무거나 " + str(len(drinks) + 2) + ")  장바구니 : " + str(len(drinks) + 3) + ")  종료 : "

def printMenu(choice):
    print(f'{drinks[choice - 1]}에 어울리는 안주는 {foods[choice - 1]} 입니다')
    print(f'가격 : {price[choice - 1]}')

def printBucket():
    for index, value in enumerate(drinks):
        print(f'{value} : {amount[index]} ')
    totalPriceLogic()
    print(f'총 가격 : {total_price}')

def totalPriceLogic():
    global total_price
    for index, value in enumerate(amount):
        total_price += price[index] * value

# dictionary 함수 리스트로 구현
{
    # print(drinks_foods.pop("고량주"))
    # for index, value in enumerate(drinks):
    #     if value=="고량주":
    #         print(foods[index])
    #         foods.remove(foods[index])
    #         drinks.remove(value)
    #         break

    # #del drinks_foods["위스키"]
    # for index, value in enumerate(drinks):
    #     if value=="위스키":
    #         foods.remove(foods[index])
    #         drinks.remove(value)
    #         break

    # drinks_foods["사케"] = "광어회"
    # count= 0
    # for index, value in enumerate(drinks):
    #     if value=="사케":
    #         foods[index] = "광어회"
    #         break
    #     count += 1
    # if count == len(drinks):
    #     drinks.append("사케")
    #     foods.append("광어회")
}

while True:
    welcomeMessageLogic()
    choice = input(welcome_message)
    total_price = 0

    if choice == str(len(drinks) + 1):
        choice = random.randint(1, len(drinks))
        choiceMenuLogic(choice)
    elif choice == str(len(drinks) + 2):
        printBucket()
    elif choice == str(len(drinks) + 3):
        totalPriceLogic()
        print(f'총 가격은 : {total_price}입니다.')
        print(f'다음에 또 오세요')
        break
    elif choice == 'kimgaegeol':
        print("관리자 모드")
        print("1) 메뉴 추가 2) 메뉴 삭제 3) 메뉴 수정 4) 끝내기")
    else:
        choiceMenuLogic(choice)

