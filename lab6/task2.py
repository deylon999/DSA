class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self._size += 1

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self._size += 1

    def delete_first(self):
        if self.head is None:
            raise IndexError("Список пуст")
        self.head = self.head.next
        self._size -= 1

    def delete_last(self):
        if self.head is None:
            raise IndexError("Список пуст")
        if self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None
        self._size -= 1

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Индекс за пределами списка")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def size(self):
        return self._size

    def __repr__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result)


ll = LinkedList()
for val in [5, 3, 5, 20]:
    ll.prepend(val)

ll.append(7)    
ll.delete_first()   
ll.delete_last()

print(ll)
print(ll.size())
