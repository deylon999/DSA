def linear_barrier(arr, target):
    arr = arr + [target]
    i = 0
    while arr[i] != target:
        i += 1
    if i < len(arr) - 1:
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


def interpolation_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right and arr[left] <= target <= arr[right]:
        if arr[left] == arr[right]:
            if arr[left] == target:
                return left
            return -1
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
    left = i // 2
    right = min(i, n - 1)
    return binary_search(arr[left:right + 1], target)


arr_sorted = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
arr_unsorted = [15, 3, 42, 7, 19, 55, 1, 28]

test_cases = [
    ("Существующий элемент (23)", 23),
    ("Первый элемент (2)",        2),
    ("Последний элемент (91)",    91),
    ("Отсутствующий элемент (99)", 99),
]

print(f"{'':<35} {'Лин':>4} {'Бин':>4} {'Инт':>4} {'Экс':>4}")

for name, target in test_cases:
    r1 = linear_barrier(arr_sorted, target)
    r2 = binary_search(arr_sorted, target)
    r3 = interpolation_search(arr_sorted, target)
    r4 = exponential_search(arr_sorted, target)
    print(f"{name:<35} {r1:>4} {r2:>4} {r3:>4} {r4:>4}")

print()
print("Линейный на неотсортированном:")
print(f"Поиск 42 -> индекс {linear_barrier(arr_unsorted, 42)}")
print(f"Поиск 99 -> индекс {linear_barrier(arr_unsorted, 99)}")