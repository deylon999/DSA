import time
import sys

def factorial_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_rec(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n - 1)


test_values = [10, 100, 500, 900]

print(f"{'n':<6} {'Цикл (сек)':>13} {'Рекурсия (сек)':>20}")

for n in test_values:
    t0 = time.perf_counter()
    for _ in range(1000):
        r_loop = factorial_loop(n)
    t_loop = (time.perf_counter() - t0) / 1000

    t0 = time.perf_counter()
    for _ in range(1000):
        r_rec = factorial_rec(n)
    t_rec = (time.perf_counter() - t0) / 1000

    print(f"{n:<6} {t_loop:>13.8f} {t_rec:>16.8f}")

try:
    factorial_rec(sys.getrecursionlimit()-1)
    print("\nвсе гуд для sys.getrecursionlimit()-1")
except RecursionError as e:
    print(f"Ошибка: {e}")

try:
    factorial_rec(sys.getrecursionlimit())
    print("\nвсе гуд для sys.getrecursionlimit()")
except RecursionError as e:
    print(f"ошибка: {e}")