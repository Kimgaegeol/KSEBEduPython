import math

# 소수 찾기 프로그램
def is_prime(num) -> bool:
    """
    소수 판정 함수  / 소수면 True, 아니면 False
    :param num: < integer >
    :return: < boolean >
    """
    if num >= 2:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
    else:
        return False

    return True

help(is_prime)

n = int(input("Input number : "))
if is_prime(n):
    print(f"{n} is prime number")
else:
    print(f"{n} is NOT prime number")


