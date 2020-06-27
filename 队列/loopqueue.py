from userqueue import Queue


class LoopQueue(Queue):
    """
    循环队列
    """

    def __init__(self, capacity=10):
        self._data = [None] * (capacity + 1)
        self._front = 1
        self._tail = 1
        self._size = 0

    def capacity(self):
        return len(self._data) - 1

    def empty(self):
        return self._front == self._tail

    def size(self):
        return self._size

    def enqueue(self, e):
        if self._tail == self._front - 1:
            self._resize(2 * self.capacity())
        self._data[self._tail] = e
        self._size += 1
        self._tail = (self._tail + 1) % len(self._data)

    def dequeue(self):
        if self.empty():
            raise IndexError('Can not dequeue from empty queue')
        e = self._data[self._front]
        self._size -= 1
        self._front = (self._front + 1) % len(self._data)
        if self.capacity() // 4 == self._size and self.capacity() // 2 != 0:
            self._resize(self.capacity() // 2)
        return e

    def front(self):
        return self._data[self._front]

    def _resize(self, capacity):
        capacity += 1
        new_data = [None] * capacity
        i = 1
        for item in self:
            new_data[i] = item
            i += 1
        self._data = new_data
        self._front = 1
        self._tail = i

    def __iter__(self):
        start = self._front
        end = self._tail
        while start != end:
            yield self._data[start]
            start = (start + 1) % len(self._data)

    def __str__(self):
        return f"{self.__class__.__name__}: size: {self._size}, capacity: {self.capacity()}\nfront [{', '.join(str(item) for item in self)}] tail"


if __name__ == '__main__':
    queue = LoopQueue()
    for i in range(10):
        queue.enqueue(i)
        print(queue)
        if i % 3 == 2:
            queue.dequeue()
            print(queue)
