import ctypes

class DynamicArray:
    def __init__(self):
        self.size = 0
        self.capacity = 2
        self._array = self._make_array(self.capacity)

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def _resize(self):
        new_capacity = self.capacity * 2
        new_array = self._make_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self._array[i]
        self._array = new_array
        self.capacity = new_capacity

    def append(self, value):
        if self.size == self.capacity:
            self._resize()
        self._array[self.size] = value
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Индекс за пределами списка")
        if self.size == self.capacity:
            self._resize()
        for i in range(self.size, index, -1):
            self._array[i] = self._array[i - 1]
        self._array[index] = value
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Индекс за пределами списка")
        for i in range(index, self.size - 1):
            self._array[i] = self._array[i + 1]
        self.size -= 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Индекс за пределами списка")
        return self._array[index]

    def __repr__(self):
        return "[" + ", ".join(str(self._array[i]) for i in range(self.size)) + "]"


da = DynamicArray()
for val in [5, 0, 1, 7, 9, 4, 6, 2, 1]:
    da.append(val)

da.insert(7, 8) 
da.delete(5) 

print(da)
print(da.size)