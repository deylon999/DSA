import random

orders_random = [57, 14, 83, 29, 61, 45, 72, 10, 34, 98, 21, 66, 39, 50, 7, 66, 28, 64, 72, 62, 66, 26, 8, 29, 89, 35, 15, 32, 27, 55, 3, 59, 100, 21, 56, 85, 36, 23, 75, 18, 49, 18, 78, 44, 59, 59, 96, 68, 23, 81, 89, 4, 25, 90, 92, 72, 8, 82, 89, 44, 82, 55, 49, 23, 49, 80, 22, 84, 67, 21, 88, 65, 73, 99, 88, 49, 92, 39, 83, 66, 83, 26, 53, 75, 56, 94, 59, 89, 71, 37, 64, 99, 96, 73, 83, 30, 79, 78, 29, 7]
orders_many_duplicates = [5, 3, 5, 2, 5, 1, 5, 4, 5, 0, 5, 3, 5, 2, 5, 1, 9, 7, 0, 10, 4, 8, 2, 6, 3, 10, 5, 1, 9, 0, 4, 7, 2, 8, 3, 6, 10, 5, 1, 9, 4, 0, 7, 2, 8, 6, 3, 10, 5, 1, 9, 0, 4, 7, 8, 2, 6, 3, 10, 5, 1, 9, 0, 4, 7, 2, 8, 6, 3, 10, 5, 1, 9, 0, 4, 7, 2, 8, 6, 3, 10, 5, 1, 9, 0, 4, 7, 2, 8, 6, 3, 10, 5, 1, 9, 0, 4, 7, 2, 8]


def get_pivot_idx(A, left, right, pivot_choice):
    if pivot_choice == "first":
        return left
    elif pivot_choice == "middle":
        return (left + right) // 2
    else:
        return random.randint(left, right)


def partition_lomuto(A, left, right, pivot_choice, stats, trace):
    pivot_idx = get_pivot_idx(A, left, right, pivot_choice)
    A[pivot_idx], A[right] = A[right], A[pivot_idx]
    pivot = A[right]
    i = left - 1

    if stats['calls'] < 3:
        trace.append(f"  Шаг {stats['calls']+1}: границы [{left}..{right}], опорный={pivot}")

    for j in range(left, right):
        stats['comparisons'] += 1
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
            stats['swaps'] += 1

    A[i + 1], A[right] = A[right], A[i + 1]
    stats['calls'] += 1

    if stats['calls'] <= 3:
        trace[-1] += f", опорный встал на позицию {i+1}"

    return i + 1


def partition_hoare(A, left, right, pivot_choice, stats, trace):
    pivot_idx = get_pivot_idx(A, left, right, pivot_choice)
    pivot = A[pivot_idx]
    i = left - 1
    j = right + 1

    if stats['calls'] < 3:
        trace.append(f"  Шаг {stats['calls']+1}: границы [{left}..{right}], опорный={pivot}")

    while True:
        i += 1
        while A[i] < pivot:
            i += 1
            stats['comparisons'] += 1
        j -= 1
        while A[j] > pivot:
            j -= 1
            stats['comparisons'] += 1
        if i >= j:
            stats['calls'] += 1
            if stats['calls'] <= 3:
                trace[-1] += f", граница разбиения={j}"
            return j
        A[i], A[j] = A[j], A[i]
        stats['swaps'] += 1


def quick_sort_lomuto(A, left, right, pivot_choice, stats, trace, depth=1):
    if left < right:
        stats['depth'] = max(stats['depth'], depth)
        p = partition_lomuto(A, left, right, pivot_choice, stats, trace)
        quick_sort_lomuto(A, left, p - 1, pivot_choice, stats, trace, depth + 1)
        quick_sort_lomuto(A, p + 1, right, pivot_choice, stats, trace, depth + 1)


def quick_sort_hoare(A, left, right, pivot_choice, stats, trace, depth=1):
    if left < right:
        stats['depth'] = max(stats['depth'], depth)
        p = partition_hoare(A, left, right, pivot_choice, stats, trace)
        quick_sort_hoare(A, left, p, pivot_choice, stats, trace, depth + 1)
        quick_sort_hoare(A, p + 1, right, pivot_choice, stats, trace, depth + 1)


def run_test(array, array_name, scheme, pivot_choice):
    A = array.copy()
    stats = {'comparisons': 0, 'swaps': 0, 'calls': 0, 'depth': 0}
    trace = []

    if scheme == "hoare":
        quick_sort_hoare(A, 0, len(A) - 1, pivot_choice, stats, trace)
    else:
        quick_sort_lomuto(A, 0, len(A) - 1, pivot_choice, stats, trace)

    print(f"\n[{array_name}] {scheme.upper()} / опорный={pivot_choice}")
    for t in trace:
        print(t)
    print(f"  сравн={stats['comparisons']}, обмены={stats['swaps']}, вызовов={stats['calls']}, макс.глубина={stats['depth']}")


for arr_name, arr in [("orders_random", orders_random), ("orders_many_duplicates", orders_many_duplicates)]:
    print(f"\n{'='*50}")
    print(f"Массив: {arr_name}")
    print('='*50)
    for scheme in ["hoare", "lomuto"]:
        for pivot in ["first", "middle", "random"]:
            run_test(arr, arr_name, scheme, pivot)