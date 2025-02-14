# decorator
# def description(f):  # closure
#     def inner(*args):
#         print(f.__name__)
#         print(f.__doc__)
#         r = f(*args)
#         return r
#
#     return inner
#
#
# def squares(n):
#     """
#     제곱 함수
#     """
#     return n * n
#
# @description
# def power(b, e):
#     """
#     거듭제곱 함수
#     """
#     result = 1
#     for _ in range(e):
#         result = result * b
#     return result
#
#
# f1 = description(squares)
# print(f1(9))
# print(power(2, 10))
# f2 = description(power)
# print(f2(2, 10))

# print(squares(7))
# print(squares.__doc__)

# 함수 안에서 return 대신 yield 를 사용하면 그 함수는 generator가 된다.
# def my_range(first=0, last=5, step=1):
#     number = first
#     while number < last:
#         yield number
#         number += step
#
# r = my_range()
# print(r, type(r))
# # x  = list(range(9))
#
# for x in r:
#     print(x) # 여기선 출력됨
# for x in my_range(1,10,1):
#     print(x) # 여기선 출력 안됨 (이미 사용하고 버려졌기 때문 / 사용된 메모리 값들은 버려짐 )

#==================================================================================================================

# def factorial_repetition(n) -> int:
#     '''
#     반복문을 이용한 팩토리얼 함수
#     :param n: 정수, int
#     :return: 팩토리얼 값, int
#     '''
#     result = 1
#     for i in range(2, n+1):
#         result = result * i
#     return result
#
# def factorial_recursion(n):
#     '''
#     재귀함수를 사용한 팩토리얼 함수
#     :param n: 정수, int
#     :return: function, int
#     '''
#     if n == 1:
#         return n
#     else:
#         return n * factorial_recursion(n-1)
#
# import time
#
# def time_decorator(f):
#     """
#     성능 측정 데코레이터
#     """
#     def wrapper(*args):
#         start = time.time()
#         result = f(*args)
#         end = time.time()
#         print(f'실행시간 : {end - start}')
#         return result
#     return wrapper
#
# def fibonacci_repetition(n):
#     list = [0, 1]
#     result = 0
#     if n==0:
#         return list[0]
#     elif n==1:
#         return list[1]
#     else:
#         for i in range(2,n+1):
#             result = list[0] + list[1]
#             list[0] = list[1]
#             list[1] = result
#         return result
#
# def fibonacci_recursion(n)->int:
#     if n ==0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci_recursion(n-2) + fibonacci_recursion(n-1)
#
# print(fibonacci_repetition(55))
#
# print(fibonacci_recursion(55))

# number = int(input("number : "))
# print(factorial_repetition(number))
# print(factorial_recursion(number))
# print(globals())

#==================================================================================================================

# def bomb_repetition(n):
#     for i in range(n, 0, -1):
#         print(i)
#     print("펑")
#
# def bomb_recursion(n):
#     if n == 0:
#         print("펑")
#     else:
#         print(n)
#         bomb_recursion(n-1)
#
# bomb_repetition(10)
# bomb_recursion(10)

#==================================================================================================================

# import random
#
# # numbers = list()
# # for i in range(5):
# #     numbers.append(random.randint(1, 100))
# numbers = [random.randint(1, 100) for i in range(10)]
# print(numbers)
#
# try:
#     # pick = int(input(f"Input index (0 ~ {len(numbers)-1}) : "))
#     # print(numbers[pick])
#     print(5/0)
# except IndexError as err:
#     print(f"Wrong index number\n{err}")
# except ValueError as err:
#     print(f"Input Only Number~\n{err}")
# except ZeroDivisionError as err:
#     print(f"The denominator cannot be 0.\n{err}")
# except Exception as err:
#     print(f"Error occurs : {err}")

#==================================================================================================================

# import random
#
# class OopsException(Exception):
#     pass
#
# # numbers = list()
# # for i in range(5):
# #     numbers.append(random.randint(1, 100))
# numbers = [random.randint(1, 100) for i in range(10)]
# print(numbers)
#
# try:
#     pick = int(input(f"Input index (0 ~ {len(numbers)-1}) : "))
#     print(numbers[pick])
#     print(5/2)
#     raise OopsException("Oops~~")  # exception!
# except IndexError as err:
#     print(f"Wrong index number\n{err}")
# except ValueError as err:
#     print(f"Input only number~\n{err}")
# except ZeroDivisionError as err:
#     print(f"The denominator cannot be 0.\n{err}")
# except OopsException as err:
#     print(f"Oops Oops {err}")
# except Exception as err:
#     print(f"Error occurs : {err}")
# else:
#     print(f"Program terminate")

# ==================================================================================================================

#class Pokemon():
# class Pokemon:
#     def __init__(self, name):
#         print(f"{name} 포켓몬스터 생성")
#
#
# pikachu = Pokemon("피카츄")
# squirtle = Pokemon("꼬부기")

# ==================================================================================================================

# class Pokemon:
#     pass
#
# pikachu = Pokemon()
# squirtle = Pokemon()
# pikachu.name = "피카츄"
# pikachu.nemesis = squirtle
# print(pikachu.name)
# #print(pikachu.nemesis.name)
# pikachu.nemesis.name = "꼬부기"  #squirtle.name = "꼬부기"
# print(pikachu.nemesis.name)
# print(squirtle.name)
#
#
# #class Pokemon():
# class Pokemon:
#     def __init__(self, name):
#         self.name = name
#         print(f"{name} 포켓몬스터 생성")
#
#     def attack(self, target):
#         print(f"{self.name}이(가) {target.name}을(를) 공격!")
#
#
#
# charizard = Pokemon("리자몽")
# pikachu = Pokemon("피카츄")
# squirtle = Pokemon("꼬부기")
# charizard.attack(squirtle)
# print(pikachu.name)
# print(squirtle.name)

# ==================================================================================================================

# class Pokemon:
#     def __init__(self, name):
#         self.name = name
#
#     def attack(self, target):
#         print(f"{self.name}이(가) {target.name}을(를) 공격!")
#
# #class Pikachu:
# class Pikachu(Pokemon):  # is-a
#     def __init__(self, name, type):
#         super().__init__(name)
#         self.type = type
#
#     def attack(self, target):
#         print(f"{self.name}이(가) {target.name}을(를) {self.type} 공격!")
#
#     def electric_info(self):
#         print("전기 계열의 공격을 합니다")
#
#
# class Squirtle(Pokemon):  # is-a
#     pass
#
# class Agumon:
#     pass
#
# p1 = Pikachu("피카츄", "전기")
# p2 = Squirtle("꼬부기")
# p3 = Pokemon("아무개")
# p1.electric_info()
# #p3.electric_info()  # AttributeError: 'Pokemon' object has no attribute 'electric_info'
# p1.attack(p2)
# p2.attack(p1)
# print(p1.name, p1.type)
# print(issubclass(Pikachu, Pokemon))
# print(issubclass(Agumon, Pokemon))

# ==================================================================================================================

class FlyingMixin:
    def fly(self):
        return f"{self.name}이(가) 하늘을 훨훨 날아갑니다~"

class SwimmingMixin:
    def swim(self):
        return f"{self.name}이(가) 수영을 합니다."

class Pokemon:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print("공격~")

class Charizard(Pokemon, FlyingMixin):
    pass

class Gyarados(Pokemon, SwimmingMixin):
    pass

g1 = Gyarados("갸라도스")
c1 = Charizard("리자몽")
# print(c1.fly())
# print(g1.swim())
# c1.attack()
# #Charizard.attack()
# Charizard.attack(c1)
print(g1.name)
g1.name = "잉어킹"
print(g1.name)

# ==================================================================================================================