cargo_priority = [42, 17, 93, 58, 11, 76, 24, 65, 39, 88, 5, 71, 30, 54, 19, 93, 7, 80, 80, 48, 77, 98, 97, 56, 27, 94, 73, 74, 72, 47, 95, 70, 96, 93, 84, 53, 38, 90, 94, 85, 34, 88, 56, 29, 65, 84, 72, 60, 63, 59, 61, 61, 14, 42, 89, 97, 62, 27, 19, 36, 18, 89, 3, 64, 99, 38, 26, 99, 55, 40, 32, 99, 86, 44, 1, 100, 53, 74, 78, 68, 21, 24, 85, 32, 99, 68, 85, 12, 4, 18, 69, 46, 46, 50, 64, 7, 68, 27, 98, 77, 41, 76, 12, 12, 62, 75, 29, 52, 12, 91, 73, 14, 22, 47, 47, 16, 25, 64, 54, 66, 89, 20, 68, 82, 4, 7, 58, 42, 13, 3, 60, 10, 52, 25, 98, 64, 86, 48, 44, 38, 2, 33, 14, 28, 29, 40, 23, 83, 47, 35]


def merge(left, right, sravneniya):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        sravneniya += 1
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result, sravneniya


def merge_sort_recursive(A, depth=0):
    if len(A) <= 1:
        return A, 0, depth

    mid = len(A) // 2
    left, s1, d1 = merge_sort_recursive(A[:mid], depth + 1)
    right, s2, d2 = merge_sort_recursive(A[mid:], depth + 1)

    merged, s3 = merge(left, right, 0)
    max_depth = max(d1, d2)

    return merged, s1 + s2 + s3, max_depth


def merge_sort_iterative(A):
    n = len(A)
    sravneniya = 0
    prokhodov = 0
    size = 1

    while size < n:
        prokhodov += 1
        for left in range(0, n, size * 2):
            mid = min(left + size, n)
            right = min(left + size * 2, n)
            if mid < right:
                merged, s = merge(A[left:mid], A[mid:right], 0)
                sravneniya += s
                A[left:right] = merged
        size *= 2

    return A, sravneniya, prokhodov



A1 = cargo_priority.copy()
sorted_A, sravneniya, max_depth = merge_sort_recursive(A1)
print(f"Рекурсивный:  сравн={sravneniya}, макс. глубина={max_depth}")

A2 = cargo_priority.copy()
sorted_A2, sravneniya2, prokhodov = merge_sort_iterative(A2)
print(f"Итерационный: сравн={sravneniya2}, проходов={prokhodov}")