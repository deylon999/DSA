import time

def power_loop(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result


def power_rec(base, exp):
    if exp == 0:          
        return 1
    if exp % 2 == 0:
        half = power_rec(base, exp // 2)    
        return half * half
    return base * power_rec(base, exp - 1)  

test_values = [100, 1000, 10000, 100000]


print(f"{'exp':<10} {'Цикл (сек)':>16} {'Рекурсия (сек)':>16}")
for exp in test_values:
    t0 = time.perf_counter()
    for _ in range(100):
        power_loop(2, exp)
    t_loop = (time.perf_counter() - t0) / 100

    t0 = time.perf_counter()
    for _ in range(100):
        power_rec(2, exp)
    t_rec = (time.perf_counter() - t0) / 100

    print(f"{exp:<10} {t_loop:>16.8f} {t_rec:>16.8f}")