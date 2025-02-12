def my_pow(x,y) -> float:
    return x**y

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

help(is_prime)

startNum = int(input("Start number : "))
endNum = int(input("End number : "))

i = startNum
while(i <= endNum):
    if is_prime(i):
        print(i)
    i += 1


# v1.1) for -> while
# v1.2) while 구문으로 구간 소수를 출력하는 프로그램 작성
# v1.3) ** 대신 pow 함수
# v1.4) my_pow함수 만들기