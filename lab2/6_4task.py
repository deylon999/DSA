import math

def is_prime(n, divisor=2):
    if n < 2:        
        return False
    if divisor > math.sqrt(n):
        return True
    if n % divisor == 0:   
        return False
    return is_prime(n, divisor + 1)


print(is_prime(7))
print(is_prime(10))
print(is_prime(97))