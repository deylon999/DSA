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

def cocktail_sort(A):
    n = len(A)
    sravneniya = 0
    obmeny = 0
    prokhodov = 0
    left = 0
    right = n - 1
    while left < right:
        prokhodov += 1
        for i in range(left, right):
            sravneniya += 1
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                obmeny += 1
        right -= 1
        for i in range(right, left, -1):
            sravneniya += 1
            if A[i] < A[i - 1]:
                A[i], A[i - 1] = A[i - 1], A[i]
                obmeny += 1
        left += 1
    return sravneniya, obmeny, prokhodov


def gnome_sort(A):
    n = len(A)
    sravneniya = 0
    obmeny = 0
    shagov = 0
    i = 0
    while i < n:
        shagov += 1
        if i == 0 or A[i] >= A[i - 1]:
            sravneniya += 1
            i += 1
        else:
            sravneniya += 1
            A[i], A[i - 1] = A[i - 1], A[i]
            obmeny += 1
            i -= 1
    return sravneniya, obmeny, shagov



datasets = [
    ("data1", [1, 2, 3, 4, 6, 5, 7, 8, 9, 10]),
    ("data2", [2, 1, 3, 4, 5, 6, 7, 8, 10, 9]),
    ("data3", [1, 3, 2, 4, 5, 7, 6, 8, 10, 9]),
    ("data4", [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
]

for name, data in datasets:
    print(f"\n=== {name} ===")

    A = data.copy()
    s, o, p = cocktail_sort(A)
    print(f"Cocktail: сравн={s}, перест={o}, проходы={p}")

    A = data.copy()
    s, o, sh = gnome_sort(A)
    print(f"Гномья:   сравн={s}, перест={o}, шаги={sh}")

    A = data.copy()
    s, o, p = bubble_sort(A)
    print(f"Пузырьк:  сравн={s}, обмены={o}, проходы={p}")