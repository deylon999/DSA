import numpy as np
import time
import matplotlib.pyplot as plt

N = 10_000
QUERIES = 500

def interpolation_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right and arr[left] <= target <= arr[right]:
        if arr[left] == arr[right]:
            return left if arr[left] == target else -1
        pos = left + (target - arr[left]) * (right - left) // (arr[right] - arr[left])
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
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

def measure_time(func, arr, queries):
    start = time.perf_counter()
    for q in queries:
        func(arr, q)
    return time.perf_counter() - start


uniform  = sorted(np.random.randint(0, 100_000, N).tolist())
quadr    = sorted(int(x**2) for x in np.linspace(0, 316, N))
expon    = sorted(int(np.exp(x)) for x in np.linspace(0, 11, N))
skewed   = sorted(np.concatenate([
    np.random.randint(0, 100, N // 2),
    np.random.randint(50_000, 100_000, N // 2)
]).tolist())

distributions = {
    "Равномерное":      uniform,
    "Квадратичное":     quadr,
    "Экспоненциальное": expon,
    "Перекошенное":     skewed,
}

print(f"{'':<20} {'Интерполяц':>17} {'Бинарный':>14}")

interp_times, binary_times, labels = [], [], []

for name, arr in distributions.items():
    queries = [arr[i] for i in np.random.randint(0, N, QUERIES)]
    t_interp = measure_time(interpolation_search, arr, queries)
    t_binary = measure_time(binary_search,        arr, queries)
    print(f"{name:<20} {t_interp:>17.6f} {t_binary:>14.6f}")
    interp_times.append(t_interp)
    binary_times.append(t_binary)
    labels.append(name)















x = np.arange(len(labels))
width = 0.35
fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(x - width/2, interp_times, width, label='Интерполяционный')
ax.bar(x + width/2, binary_times,  width, label='Бинарный')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Время (с)')
ax.set_title('Интерполяционный vs Бинарный поиск\nпри разных распределениях')
ax.legend()
plt.tight_layout()
plt.savefig('task2_distributions.png', dpi=150)
plt.show()