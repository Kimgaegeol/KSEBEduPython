import math

def my_pow(b, e) -> float:
    """

    :param b:
    :param e:
    :return:
    """
    result = 1

    i = int(e)
    f = e - i

    for _ in range(i):
        result = result * b


    if f > 0:
        result = result * math.exp(f * math.log(b))

    return result

print(my_pow(2,-1))
print(my_pow(5,0.3))