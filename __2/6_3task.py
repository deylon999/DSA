import random

def multiply_random(n):
    if n == 0:
        return 0
    return n * random.random()


print(multiply_random(10))