import random
import time
import matplotlib.pyplot as plt

N = 10_000

def linear_search(arr, target):
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1

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

arr = random.sample(range(N * 10), N)
K_values = list(range(1, 201, 5))
linear_times, sort_binary_times = [], []

for K in K_values:
    queries = [random.choice(arr) for _ in range(K)]

    start = time.perf_counter()
    for q in queries:
        linear_search(arr, q)
    linear_times.append(time.perf_counter() - start)

    start = time.perf_counter()
    sorted_arr = sorted(arr)
    for q in queries:
        binary_search(sorted_arr, q)
    sort_binary_times.append(time.perf_counter() - start)

threshold = None
for i, K in enumerate(K_values):
    if sort_binary_times[i] < linear_times[i]:
        threshold = K
        break

print(f"Порог: K = {threshold}")








plt.figure(figsize=(9, 5))
plt.plot(K_values, linear_times,     label='Linear total',       linewidth=2)
plt.plot(K_values, sort_binary_times, label='Sort + Binary total', linewidth=2)
if threshold:
    plt.axvline(threshold, color='red', linestyle='--', label=f'Порог K={threshold}')
plt.xlabel('Число запросов K')
plt.ylabel('Время (с)')
plt.title('Линейный поиск vs Сортировка + Бинарный поиск')
plt.legend()
plt.tight_layout()
plt.savefig('task3_threshold.png', dpi=150)
plt.show()