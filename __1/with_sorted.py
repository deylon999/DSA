import time
import random
import matplotlib.pyplot as plt

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

n_values = [1000, 2000, 5000, 10000]
bubble_times = []
sorted_times = []

print(f"{'n':<10} {'Bubble (s)':<15} {'Sorted (s)':<15}")

for n in n_values:
    data = [random.randint(0, 100000) for _ in range(n)]
    
    data_bubble = data.copy()
    start = time.perf_counter()
    bubble_sort(data_bubble)
    t_bubble = time.perf_counter() - start
    bubble_times.append(t_bubble)
    
    data_sorted = data.copy()
    start = time.perf_counter()
    sorted(data_sorted)
    t_sorted = time.perf_counter() - start
    sorted_times.append(t_sorted)
    
    print(f"{n:<10} {t_bubble:<15.6f} {t_sorted:<15.6f}")