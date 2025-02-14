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

def factorial_repetition(n) -> int:
    '''
    반복문을 이용한 팩토리얼 함수
    :param n: 정수, int
    :return: 팩토리얼 값, int
    '''
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result

def factorial_recursion(n):
    '''
    재귀함수를 사용한 팩토리얼 함수
    :param n: 정수, int
    :return: function, int
    '''
    if n == 1:
        return n
    else:
        return n * factorial_recursion(n-1)

def fibonacci(n):
    list = [0, 1]
    result = 0
    if n==0:
        return list[0]
    elif n==1:
        return list[1]
    else:
        for i in range(2,n+1):
            result = list[0] + list[1]
            list[0] = list[1]
            list[1] = result
        return result

def fibonacci_recursion(n)->int:
    if n ==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursion(n-2) + fibonacci_recursion(n-1)

print(fibonacci(8))

# number = int(input("number : "))
# print(factorial_repetition(number))
# print(factorial_recursion(number))
# print(globals())

#==================================================================================================================