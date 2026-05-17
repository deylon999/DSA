from task1 import DynamicArray
from task2 import LinkedList

import time

def measure(func, *args):
    start = time.perf_counter()
    result = func(*args)
    return time.perf_counter() - start, result

def benchmark(N):
    results = {}

    da = DynamicArray()
    for i in range(N):
        da.append(i)

    t, _ = measure(da.append, 999)
    results["array_append"] = t

    t, _ = measure(da.delete, 0)
    results["array_delete_first"] = t

    t, _ = measure(da.get, N // 2)
    results["array_get"] = t

    t, _ = measure(lambda: da.size, )
    results["array_size"] = t

    ll = LinkedList()
    for i in range(N):
        ll.append(i)

    t, _ = measure(ll.append, 999)
    results["ll_append"] = t

    t, _ = measure(ll.delete_first)
    results["ll_delete_first"] = t

    t, _ = measure(ll.get, N // 2)
    results["ll_get"] = t

    t, _ = measure(ll.size)
    results["ll_size"] = t

    return results

sizes = [100, 1000, 10000]
ops = ["append", "delete_first", "get", "size"]
labels = {
    "append":       "Добавление в конец",
    "delete_first": "Удаление из начала",
    "get":          "Доступ по индексу ",
    "size":         "Получение размера  ",
}

header = f"{'Операция':<22} {'Структура':<15} " + "".join(f"N={n:<10}" for n in sizes)
print(header)

all_results = {n: benchmark(n) for n in sizes}

for op in ops:
    for struct, key in [("Массив", f"array_{op}"), ("Св. список", f"ll_{op}")]:
        row = f"{labels[op]:<22} {struct:<10}"
        row += "".join(f"{all_results[n][key]*1e6:>8.2f} мкс" for n in sizes)
        print(row)
    print()
