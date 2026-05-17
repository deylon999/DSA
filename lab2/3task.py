text = open("text.txt", encoding="utf-8").read()

def count_spaces_loop(s):
    count = 0
    for char in s:
        if char == " ":
            count += 1
    return count


def count_spaces_rec(s):
    if len(s) == 0:
        return 0
    return (1 if s[0] == " " else 0) + count_spaces_rec(s[1:])

print(f"Цикл:     {count_spaces_loop(text)}")
print(f"Рекурсия: {count_spaces_rec(text)}")