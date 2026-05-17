from task2 import LinkedList  

class Stack:
    def __init__(self):
        self._list = LinkedList()

    def push(self, value):
        self._list.prepend(value)

    def pop(self):
        if self._list.size() == 0:
            raise IndexError("Стек пуст")
        value = self._list.get(0)
        self._list.delete_first()
        return value

    def peek(self):
        if self._list.size() == 0:
            raise IndexError("Стек пуст")
        return self._list.get(0)

    def size(self):
        return self._list.size()

stack = Stack()
for val in [5, 0, 1, 7, 9]:
    stack.push(val)

print("Верхний элемент:", stack.peek())
stack.pop()
stack.pop()
print("Верхний элемент после двух pop:", stack.peek())
print("Итоговый размер стека:", stack.size())
