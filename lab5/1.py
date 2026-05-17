def bubble_sort(A):
    n = len(A)
    sravneniya = 0
    obmeny = 0
    prokhodov = 0

    for i in range(n - 1):
        prokhodov += 1
        for j in range(n - 1 - i):
            sravneniya += 1
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                obmeny += 1

    return sravneniya, obmeny, prokhodov


def selection_sort(A):
    n = len(A)
    sravneniya = 0
    obmeny = 0
    prokhodov = 0

    for i in range(n - 1):
        prokhodov += 1
        min_idx = i

        for j in range(i + 1, n):
            sravneniya += 1
            if A[j] < A[min_idx]:
                min_idx = j

        A[i], A[min_idx] = A[min_idx], A[i]
        obmeny += 1

    return sravneniya, obmeny, prokhodov


def insertion_sort(A):
    n = len(A)
    sravneniya = 0
    sdvigi = 0
    prokhodov = 0

    for i in range(1, n):
        prokhodov += 1
        key = A[i]
        j = i - 1

        while j >= 0:
            sravneniya += 1
            if A[j] > key:
                A[j + 1] = A[j]
                sdvigi += 1
                j -= 1
            else:
                break

        A[j + 1] = key

    return sravneniya, sdvigi, prokhodov




data_random = [57, 12, 89, 34, 76, 11, 90, 43, 65, 28, 71, 5, 39, 84, 22]
data_sorted = [5, 11, 12, 22, 28, 34, 39, 43, 57, 65, 71, 76, 84, 89, 90]
data_reverse = [90, 89, 84, 76, 71, 65, 57, 43, 39, 34, 28, 22, 12, 11, 5]
data_almost_sorted = [5, 11, 12, 22, 28, 34, 43, 39, 57, 65, 71, 76, 84, 89, 90]

datasets = [
    ("data_random", data_random),
    ("data_sorted", data_sorted),
    ("data_reverse", data_reverse),
    ("data_almost_sorted", data_almost_sorted),
]

for name, data in datasets:
    print(f"\n=== {name} ===")

    A = data.copy()
    s, o, p = bubble_sort(A)
    print(f"Пузырьковая:  сравн={s}, обмены={o}, проходы={p}")

    A = data.copy()
    s, o, p = selection_sort(A)
    print(f"Выборочная:   сравн={s}, обмены={o}, проходы={p}")

    A = data.copy()
    s, sd, p = insertion_sort(A)
    print(f"Вставками:    сравн={s}, сдвиги={sd}, проходы={p}")