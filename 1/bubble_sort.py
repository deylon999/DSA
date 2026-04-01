import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

sizes = [100, 200, 400, 800, 1600, 3200]

print(f"{'n':<10} {'n^2':<12} {'Среднее время':<20}")

for n in sizes:
    times = []
    for _ in range(5):
        data = [random.randint(0, 10000) for _ in range(n)]
        start = time.perf_counter()
        bubble_sort(data)
        times.append(time.perf_counter() - start)
    
    avg_time = sum(times) / 5
    print(f"{n:<10} {n*n:<12} {avg_time:<20.6f}")