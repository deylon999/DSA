def linear_barrier_stats(arr, target):
    arr = arr + [target]
    i = 0
    comparisons = iterations = 0
    while arr[i] != target:
        comparisons += 1
        iterations  += 1
        i += 1
    comparisons += 1
    iterations  += 1
    found = i if i < len(arr) - 1 else -1
    return found, {"comparisons": comparisons, "iterations": iterations, "shifts": i}


def binary_search_stats(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = iterations = shifts = 0
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, {"comparisons": comparisons, "iterations": iterations, "shifts": shifts}
        elif arr[mid] < target:
            left = mid + 1
            shifts += 1
        else:
            right = mid - 1
            shifts += 1
    return -1, {"comparisons": comparisons, "iterations": iterations, "shifts": shifts}


def interpolation_search_stats(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = iterations = shifts = 0
    while left <= right and arr[left] <= target <= arr[right]:
        iterations += 1
        if arr[left] == arr[right]:
            comparisons += 1
            return (left, {"comparisons": comparisons, "iterations": iterations, "shifts": shifts}) \
                   if arr[left] == target else \
                   (-1, {"comparisons": comparisons, "iterations": iterations, "shifts": shifts})
        pos = left + (target - arr[left]) * (right - left) // (arr[right] - arr[left])
        comparisons += 1
        if arr[pos] == target:
            return pos, {"comparisons": comparisons, "iterations": iterations, "shifts": shifts}
        elif arr[pos] < target:
            left = pos + 1
            shifts += 1
        else:
            right = pos - 1
            shifts += 1
    return -1, {"comparisons": comparisons, "iterations": iterations, "shifts": shifts}


def exponential_search_stats(arr, target):
    n = len(arr)
    comparisons = iterations = shifts = 1
    if arr[0] == target:
        return 0, {"comparisons": 1, "iterations": 1, "shifts": 0}
    i = 1
    while i < n and arr[i] <= target:
        iterations += 1
        comparisons += 1
        shifts += 1
        i *= 2
    left, right = i // 2, min(i, n - 1)
    idx, stats = binary_search_stats(arr[left:right + 1], target)
    total = {k: v + stats[k] for k, v in
             {"comparisons": comparisons, "iterations": iterations, "shifts": shifts}.items()}
    return (left + idx if idx != -1 else -1), total


arr = [1, 3, 5, 7, 9, 11, 14, 18, 22, 27, 35, 44, 58, 73, 91]
test_targets = [7, 44, 1, 91, 99]

header = f"{'Цель':>5} | {'Алгоритм':<25} | {'Результат':>10} | {'Сравн.':>7} | {'Итер.':>6} | {'Сдвиги':>7}"
print(header)

funcs = [
    ("Линейный (барьер)",     linear_barrier_stats),
    ("Бинарный",              binary_search_stats),
    ("Интерполяционный",      interpolation_search_stats),
    ("Экспоненциальный",      exponential_search_stats),
]

for target in test_targets:
    for name, func in funcs:
        idx, stats = func(arr, target)
        print(f"{target:>5} {name:<25} {idx:>10} "
              f"{stats['comparisons']:>7} {stats['iterations']:>6} {stats['shifts']:>7}")
    print()