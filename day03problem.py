import random

def printMenu(menu):
    try:
        choice = int(menu)
        print(choice)
        if 1 <= choice and choice <= len(drinks):
            print(f'{drinks[choice - 1]}에 어울리는 안주는 {foods[choice - 1]} 입니다')
            return
    except Exception as e:
        print(e)

drinks = ["위스키","와인","소주","고량주"]
foods = ["초콜릿","치즈","삼겹살","양꼬치"]
price = [50000,30000,5000,7500]

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

#drinks_foods["사케"] = "광어회"
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
    menu = 0
    menuText = "다음 술중에 고르세요.\n"
    for index, value in enumerate(drinks):
        menuText += str(index + 1) + ") " +  value + "  "
    menuText +=  str(len(drinks) + 1) + ")  아무거나 " + str(len(drinks) + 2) + ")  종료 : "

    menu = input(menuText)

    if menu == str(len(drinks) + 1):
        menu = random.randint(1,len(drinks))
        printMenu(menu)
    elif menu == str(len(drinks) + 2):
        print(f'다음에 또 오세요')
        break
    else:
        printMenu(menu)

