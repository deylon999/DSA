import random
import time
import bisect
import numpy as np
import matplotlib.pyplot as plt

N = 100_000
QUERIES = 1_000

arr_list = sorted(random.sample(range(N * 10), N))
arr_np   = np.array(arr_list)
queries  = [random.choice(arr_list) for _ in range(QUERIES)]


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


results = {}

start = time.perf_counter()
for q in queries:
    binary_search(arr_list, q)
results["Свой бинарный"] = time.perf_counter() - start

start = time.perf_counter()
for q in queries:
    arr_list.index(q) if q in arr_list else -1
results["in + .index()"] = time.perf_counter() - start

start = time.perf_counter()
for q in queries:
    bisect.bisect_left(arr_list, q)
results["bisect"] = time.perf_counter() - start

start = time.perf_counter()
for q in queries:
    np.searchsorted(arr_np, q)
results["numpy.searchsorted"] = time.perf_counter() - start


print(f"\n{'Метод':<25} {'Время (с)':>12} {'Запр/сек':>12}")
for name, t in results.items():
    rps = QUERIES / t
    print(f"{name:<25} {t:>12.6f} {rps:>12.0f}")






plt.figure(figsize=(8, 5))
plt.bar(results.keys(), results.values(), color=['steelblue','orange','green','red'])
plt.ylabel('Время (с)')
plt.title(f'Сравнение методов поиска (N={N}, запросов={QUERIES})')
plt.tight_layout()
plt.savefig('task5_comparison.png', dpi=150)
plt.yscale('log')
plt.show()