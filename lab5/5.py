records1 = [("A1", 4), ("A2", 2), ("A3", 4), ("A4", 1), ("A5", 3), ("A6", 2), ("A7", 4), ("A8", 1), ("A9", 3), ("A10", 2)]
records2 = [("B1", 5), ("B2", 5), ("B3", 5), ("B4", 2), ("B5", 2), ("B6", 3), ("B7", 3), ("B8", 3), ("B9", 1), ("B10", 1)]
records3 = [("C1", 3), ("C2", 1), ("C3", 3), ("C4", 2), ("C5", 3), ("C6", 1), ("C7", 2), ("C8", 3), ("C9", 1), ("C10", 2), ("C11", 3), ("C12", 1)]


def check_stability(original, sorted_arr):
    for i in range(len(sorted_arr) - 1):
        for j in range(i + 1, len(sorted_arr)):
            if sorted_arr[i][1] == sorted_arr[j][1]:
                orig_i = original.index(sorted_arr[i])
                orig_j = original.index(sorted_arr[j])
                if orig_i > orig_j:
                    return False
    return True


def bubble_sort_records(A):
    A = A.copy()
    n = len(A)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if A[j][1] > A[j + 1][1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A


def insertion_sort_records(A):
    A = A.copy()
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j][1] > key[1]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A


def selection_sort_records(A):
    A = A.copy()
    n = len(A)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if A[j][1] < A[min_idx][1]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
    return A


def quick_sort_records(A, left, right):
    if left < right:
        pivot = A[right][1]
        i = left - 1
        for j in range(left, right):
            if A[j][1] <= pivot:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[right] = A[right], A[i + 1]
        p = i + 1
        quick_sort_records(A, left, p - 1)
        quick_sort_records(A, p + 1, right)


algorithms = [
    ("Пузырьковая", bubble_sort_records),
    ("Вставками",   insertion_sort_records),
    ("Выборочная",  selection_sort_records),
]

datasets = [
    ("records1", records1),
    ("records2", records2),
    ("records3", records3),
]


for rec_name, records in datasets:
    print(f"\n=== {rec_name} ===")
    print(f"Исходный: {records}")

    for alg_name, alg_func in algorithms:
        result = alg_func(records)
        stable = check_stability(records, result)
        print(f"{alg_name}: {result}")
        print(f"  Устойчива: {stable}")

    A = records.copy()
    quick_sort_records(A, 0, len(A) - 1)
    stable = check_stability(records, A)
    print(f"Быстрая: {A}")
    print(f"  Устойчива: {stable}")

print("\n=== Многокритериальная сортировка (records1) ===")

step1 = insertion_sort_records([(r[0], ord(r[0][0])*100 + int(r[0][1:])) for r in records1])
step1 = [(r[0], dict(records1)[r[0]]) for r in step1]
step2_stable = insertion_sort_records(step1)
print(f"Устойчивая (вставками): {step2_stable}")

step1 = records1.copy()
step1.sort(key=lambda x: x[0])
A = step1.copy()
quick_sort_records(A, 0, len(A) - 1)
print(f"Неустойчивая (быстрая): {A}")