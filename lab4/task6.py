import random
import time
import matplotlib.pyplot as plt

SIZES   = [1_000, 10_000, 100_000, 1_000_000]
QUERIES = 200


def linear_barrier(arr, target):
    arr = arr + [target]
    i = 0
    while arr[i] != target:
        i += 1
    return i if i < len(arr) - 1 else -1


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


def exponential_search(arr, target):
    n = len(arr)
    if arr[0] == target:
        return 0
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    return binary_search(arr[i // 2: min(i, n - 1) + 1], target)

algos = {
    "Линейный":        linear_barrier,
    "Бинарный":        binary_search,
    "Интерполяционный": interpolation_search,
    "Экспоненциальный": exponential_search,
}

times = {name: [] for name in algos}

print(f"{'N':>10}", end="")
for name in algos:
    print(f"  {name:>17}", end="")
print()

for N in SIZES:
    arr = sorted(random.sample(range(N * 10), N))
    queries = [random.choice(arr) for _ in range(QUERIES)]
    print(f"{N:>10}", end="")
    for name, func in algos.items():
        start = time.perf_counter()
        for q in queries:
            func(arr, q)
        avg = (time.perf_counter() - start) / QUERIES
        times[name].append(avg)
        print(f"  {avg:>17.8f}", end="")
    print()






plt.figure(figsize=(10, 6))
for name, vals in times.items():
    plt.plot(SIZES, vals, marker='o', label=name, linewidth=2)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Размер массива N (лог. шкала)')
plt.ylabel('Среднее время поиска (с, лог. шкала)')
plt.title('Влияние размера массива на время поиска')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('task6_sizes.png', dpi=150)
plt.show()