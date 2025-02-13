# import random
#
# drinks = ["위스키", "와인", "소주", "고량주"]
# foods = ["초콜릿", "치즈", "삼겹살", "양꼬치"]
# price = [50000, 30000, 5000, 20000]
# total_price = 0
#
# drinks.append("사케")
# foods.append("광어")
# price.append(10000)
#
# amount = [0 for menu in drinks]
#
# welcome_message = ""
# choice = 0
#
# def choiceMenuLogic(choice):
#     try:
#         global total_price
#         choice = int(choice)
#         if 1 <= choice and choice <= len(drinks):
#             amount[choice - 1] += 1
#             printMenu(choice)
#             return
#     except Exception as e:
#         print("잘못된 입력입니다.")
#
# def welcomeMessageLogic():
#     global welcome_message
#     welcome_message = "다음 술중에 고르세요.\n"
#     for index, value in enumerate(drinks):
#         welcome_message += str(index + 1) + ") " + value + "  "
#     welcome_message += str(len(drinks) + 1) + ")  아무거나 " + str(len(drinks) + 2) + ")  장바구니 : " + str(len(drinks) + 3) + ")  종료 : "
#
# def printMenu(choice):
#     print(f'{drinks[choice - 1]}에 어울리는 안주는 {foods[choice - 1]} 입니다')
#     print(f'가격 : {price[choice - 1]}')
#
# def printBucket():
#     for index, value in enumerate(drinks):
#         print(f'{value} : {amount[index]} ')
#     totalPriceLogic()
#     print(f'총 가격 : {total_price}')
#
# def totalPriceLogic():
#     global total_price
#     for index, value in enumerate(amount):
#         total_price += price[index] * value
#
# # dictionary 함수 리스트로 구현
# {
#     # print(drinks_foods.pop("고량주"))
#     # for index, value in enumerate(drinks):
#     #     if value=="고량주":
#     #         print(foods[index])
#     #         foods.remove(foods[index])
#     #         drinks.remove(value)
#     #         break
#
#     # #del drinks_foods["위스키"]
#     # for index, value in enumerate(drinks):
#     #     if value=="위스키":
#     #         foods.remove(foods[index])
#     #         drinks.remove(value)
#     #         break
#
#     # drinks_foods["사케"] = "광어회"
#     # count= 0
#     # for index, value in enumerate(drinks):
#     #     if value=="사케":
#     #         foods[index] = "광어회"
#     #         break
#     #     count += 1
#     # if count == len(drinks):
#     #     drinks.append("사케")
#     #     foods.append("광어회")
# }
#
# while True:
#     welcomeMessageLogic()
#     choice = input(welcome_message)
#     total_price = 0
#
#     if choice == str(len(drinks) + 1):
#         choice = random.randint(1, len(drinks))
#         choiceMenuLogic(choice)
#     elif choice == str(len(drinks) + 2):
#         printBucket()
#     elif choice == str(len(drinks) + 3):
#         totalPriceLogic()
#         print(f'총 가격은 : {total_price}입니다.')
#         print(f'다음에 또 오세요')
#         break
#     elif choice == 'kimgaegeol':
#         print("관리자 모드")
#         print("1) 메뉴 추가 2) 메뉴 삭제 3) 메뉴 수정 4) 끝내기")
#     else:
#         choiceMenuLogic(choice)
#
# import time


#====================================================================================================================

# def squares(*n) -> list:
#     """
#     넘겨 받은 수치 데이터들의 거듭제곱 값을 리스트에 담아서 리턴
#     :param n: tuple
#     :return: list
#     """
#     return [pow(i, 2) for i in n]
#     #return n * n
#
#
# def run_function(f, *number) -> list:
#     return f(*number)
#
# print(squares(7, 5, 2))
# # print(run_function(squares, 9, 10))
#
# # 파이썬에서 함수는 first citizen 이다
# # 그 이유는 파이썬에서 함수는 매개변수로 던져질 수 있고, 첫 번째로 던져져야 하기 때문

#====================================================================================================================

# closure
# def out_func(nout):
#     def inner_func():
#         return nout * nout
#     return inner_func
#
# x = out_func(9)
# print(type(x))
# print(x)
# print(x())

# inner function
# def out_func(nout):
#     def inner_func(nin):
#         return nin * nin
#     return inner_func(nout)
#
# print(out_func(5))

#====================================================================================================================

# numbers = ["7", "-11", "3"]
# ns = list()
# print(sum(map(float, numbers)))

# for  n in range(len(numbers)):
#     ns.append(int(numbers[n]))
# print(sum(ns))

# numbers = ["7", "-11", "3"]
# hap = 0
# for number in numbers:
#     hap = hap + int(number)
# print(hap)

#====================================================================================================================

# prime number with function
# def isprime(n) -> bool:
#     """
#     매개변수로 넘겨 받은 수가 소수인지 여부를 boolean으로 리턴
#     :param n: 판정할 매개변수
#     :return: 소수면 True, 소수가 아니면 False
#     """
#     if n < 2:
#         return False
#     else:
#         i = 2
#         while i*i <= n:
#             if n % i == 0:
#                 return False
#             i += 1
#         return True
#
#
# while True:
#     menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Prime1   4) Prime2   5) Quit program : ")
#
#     if menu == '1':
#         fahrenheit = float(input('Input Fahrenheit : '))
#         print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit-32.0)*5.0/9.0):.4f}C')
#     elif menu == '2':
#         celsius = float(input('Input Celsius : '))
#         print(f'Celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')
#     elif menu == '3':
#         number = int(input("Input number : "))
#         if isprime(number):
#             print(f'{number} is prime number')
#         else:
#             print(f'{number} is NOT prime number!')
#     elif menu == '4':
#         n1, n2 = map(int, input("Input first second number : ").split())
#         n1, n2 = min(n1, n2), max(n1, n2)
#         # numbers = input("Input first second number : ").split()
#         # n1 = int(numbers[0])
#         # n2 = int(numbers[1])
#         # if n1 > n2:
#         #     n1, n2 = n2, n1
#
#         for number in range(n1, n2 + 1):
#             if isprime(number):
#                 print(number, end=' ')
#         print()
#     elif menu == '5':
#         print('Terminate Program.')
#         break
#     else:
#         print('Invalid Menu!')

# ====================================================================================================================

# def squares(n):
#     return n * n

# even_numbers = [i for i in range(51) if i % 2 == 0]
# print(even_numbers)
#print(tuple(map(squares, even_numbers)))

#print(tuple(map(lambda x: x**2, even_numbers)))
# z = lambda x: pow(x, 2)
# print(tuple(map(z, even_numbers)))

# ns = [-9,7,-11,988]
# print(tuple(map(abs,ns)))

# ====================================================================================================================
# import time
#
# def time_decorator(func):
#     def wrapper(*arg):
#         s = time.time()
#         r = func(*arg)
#         e = time.time()
#         print(f'실행시간 : {e-s}초')
#         return r
#     return wrapper
#
# @time_decorator
# def factorial_repetition(n) -> int:
#     result = 1
#     for i in range(2, n+1):
#         result = result * i
#     return result
#
# number = int(input())
# print(f'{number}! = {factorial_repetition(number)} ')
#
# s = time.time()
# print(f"{number}! = {factorial_repetition(number)}")
# e = time.time()
# print(e-s)

# ====================================================================================================================

# decorator
def description(f):  # closure
    def inner(*args):
        print(f.__name__)
        print(f.__doc__)
        r = f(*args)
        return r

    return inner

def squares(n):
    """
    제곱 함수
    """
    return n * n

# @description # power 함수 호출 시 무조건 description decorator 실행됨
def power(b, e):
    """
    거듭제곱 함수
    """
    result = 1
    for _ in range(e):
        result = result * b
    return result


# print(squares(7))
f1 = description(squares) # f1은 이너함수의 주소 / f1()은 이너 함수로서 작용 / f1(9)은 이너 함수에 9를 넣은 값
print(f1())

# print(power(2, 10))
# f2 = description(power)
# print(f2(2, 10))

# print(squares(7))
# print(squares.__doc__)

# def my_range(first=0, last=5, step=1):
#     number = first
#     while number < last:
#         yield number
#         number += step
#
# r = my_range()
# print(r, type(r))
#
# for x in r:
#     print(x)
# for x in r:
#     print(x)

# ====================================================================================================================


# Assignment
# 2중 데코레이터 적용( 성능 측정 데코레이터, 디스크립션 데코레이터 ) 를 팩토리얼 함수에 적용하시오.