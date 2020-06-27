from userqueue import Queue
from myarray import Array


class ArrayQueue(Queue):
    """
    基于数值实现的队列
    """

    def __init__(self, seq=None, capacity=10):
        self._array = Array(seq, capacity)

    def enqueue(self, e):
        self._array.add_last(e)

    def dequeue(self):
        return self._array.remove_first()

    def front(self):
        return self._array.get_first()

    def size(self):
        return self._array.get_size()

    def empty(self):
        return self._array.is_empty()

    def capacity(self):
        return self._array.get_capacity()

    def __repr__(self):
        return f"{self.__class__.__name__}: front [ {', '.join(str(item) for item in self._array)} ]"


if __name__ == '__main__':
    queue = ArrayQueue()
    for i in range(5):
        queue.enqueue(i)
        print(queue)
    print(queue.dequeue())
    print(queue)
