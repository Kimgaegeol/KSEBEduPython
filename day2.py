import math

# dan  =  int(input("Input dan : "))
#
# # for dan in range(2,10,1):
# for i in range(1,10):
#     print(f"{dan} * {i} = {dan*i}")

# 소수 찾기 프로그램
n = int(input("Input number : "))
is_prime = True

if  n > 1:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
        print(i, " ")

    if is_prime:
        print(f"{n} is prime number")
    else:
        print(f"{n} is NOT prime number")

else:
    print(f"{n} is NOT prime number")
