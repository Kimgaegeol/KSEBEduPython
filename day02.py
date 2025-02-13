import math

"you coding noob"
def my_pow(b, e) -> float:
    """

    :param b:
    :param e:
    :return:
    """

    result = 1

    if e == 0:
        pass
    elif e > 0:

        i = int(e)
        f = e - i

        for _ in range(i):
            result = result * b


        if f > 0:
            result = result * math.exp(f * math.log(b))

    else:
        i = int(-e)
        f = -e -  i

        for _ in range(i):
            result = result * b


        if f > 0:
            result =result * math.exp(f * math.log(b))

        result =  1/ result

    return result


def is_prime(num) -> bool:
    """
    소수 판정 함수  / 소수면 True, 아니면 False
    :param num: < integer >
    :return: < boolean >
    """
    if num >= 2:
        i = 2
        while(i <= int(my_pow(num,0.5)) + 1 ):
            if num % i == 0:
                return False
            i += 1
    else:
        return False

    return True

# help(is_prime)
#
# startNum = int(input("Start number : "))
# endNum = int(input("End number : "))
#
# i = startNum
#
# while(i <= endNum):
#     if is_prime(i):
#         print(i)
#     i += 1

# print(my_pow(3,-1))

# v1.1) for -> while
# v1.2) while 구문으로 구간 소수를 출력하는 프로그램 작성
# v1.3) ** 대신 pow 함수
# v1.4) my_pow함수 만들기

#===============================================================================================================================

# univ = "Inha university"
# print(univ)
# print(univ[5])
# univ[5] = 'U'  # immutable
# print(univ)
# subjects = ['python', 'c++', 'linux', 'data structure', 'database']
# print(subjects)
# print(subjects[3])
# subjects[3] = 'data structure & algorithm'  # mutable
# print(subjects)

# print(0.1)
# print(1e-1)
# print(0.01)
# print(1e-2)
# print(314.1592)
# print(0.3141592e3)
# print(21000)
# print(21_000)

#===============================================================================================================================