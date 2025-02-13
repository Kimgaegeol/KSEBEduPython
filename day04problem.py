import time

def time_decorator(f):
    """
    성능 측정 데코레이터
    """
    def wrapper(*args):
        print("timewrapper 실행")
        start = time.time()
        result = f(*args)
        end = time.time()
        print(f'실행시간 : {end - start}')
        return result
    return wrapper

def description_decorator(f):
    """
    설명 출력 데코레이터
    """
    def wrapper(*args):
        print("description decorator 실행")
        print(f.__name__)
        print(f.__doc__)
        result = f(*args)
        print("description decorator 끝")
        return result
    return wrapper

def factorial(number) -> int:
    """
    팩토리얼 함수
    """
    print("factorial 함수 실행")
    result = 1
    for i in range(2,number+1):
        result *= i
    print("factorial 함수 끝")

    return result

if __name__ == '__main__':
    f1 = time_decorator(description_decorator(factorial))
    # f2 = description_decorator(time_decorator(factorial))
    print(f1(5))
    # print()
    # print()
    # print(f2(5))