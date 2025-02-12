import random

def printMenu(menu):
    choice = int(menu)
    print(f'{drinks[choice-1]}에 어울리는 안주는 {foods[choice-1]} 입니다')

drinks = ["위스키","와인","소주","고량주","사케"]
foods = ["초콜릿","치즈","삼겹살","양꼬치","광어"]

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
    menu = input(f'다음 술중에 고르세요.\n1) {drinks[0]}   2) {drinks[1]}   3) {drinks[2]}   4) {drinks[3]}   5) {drinks[4]}   6) 아무거나   7) 종료 : ')
    if menu == '6':
        menu = random.randint(1,5)
        printMenu(menu)
    elif menu == '7':
        print(f'다음에 또 오세요')
        break
    else:
        printMenu(menu)
