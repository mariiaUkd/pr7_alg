class ArrayQueue:
    def __init__(self, capacity=13):
        self._size = capacity + 1
        self._data = [None] * self._size
        self._head = 0  
        self._tail = 0  

    def is_empty(self):
        return self._head == self._tail

    def is_full(self):
        return (self._tail + 1) % self._size == self._head

    def size(self):
        return (self._tail - self._head) % self._size

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Черга переповнена")
        self._data[self._tail] = value
        self._tail = (self._tail + 1) % self._size  

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Черга порожня")
        value = self._data[self._head]
        self._data[self._head] = None
        self._head = (self._head + 1) % self._size 
        return value

    def display(self):
        items = []
        i = self._head
        while i != self._tail:
            items.append(self._data[i])
            i = (i + 1) % self._size
        print("Черга (масив):", items if items else "порожня")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  


class LinkedQueue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    def is_empty(self):
        return self._head is None

    def size(self):
        return self._count

    def enqueue(self, value):
        node = Node(value)
        if self._tail is None:
            self._head = node
        else:
            self._tail.next = node 
        self._tail = node
        self._count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Черга порожня")
        node = self._head
        self._head = node.next 
        if self._head is None:
            self._tail = None
        self._count -= 1
        return node.data

    def display(self):
        items = []
        cur = self._head
        while cur:
            items.append(cur.data)
            cur = cur.next
        print("Черга (вузли):", items if items else "порожня")


def demo(queue):
    queue.display()
    print("Кількість елементів:", queue.size())

    for x in (6, 4, 6, 2, 7):
        queue.enqueue(x)
        print(f"Додано {x}")
    queue.display()
    print("Кількість елементів:", queue.size())

    print("Видалено:", queue.dequeue())
    print("Видалено:", queue.dequeue())
    queue.display()
    print("Кількість елементів:", queue.size())

    queue.enqueue(9)
    print("Додано 9")
    queue.display()

    while not queue.is_empty():
        print("Видалено:", queue.dequeue())
    queue.display()
    print("Кількість елементів:", queue.size())

    try:
        queue.dequeue()
    except IndexError as e:
        print("Помилка:", e)


if __name__ == "__main__":
    print("=== Черга на масиві ===")
    demo(ArrayQueue())
    print("\n=== Черга на вузлах ===")
    demo(LinkedQueue())