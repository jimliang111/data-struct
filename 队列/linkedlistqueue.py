from queue import Queue


class LinkedListQueue(Queue):

    class Node:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next = next_node

        def __repr__(self):
            return str(self.value)

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, value):
        if self.empty():
            self._head = self.Node(value)
            self._tail = self._head
        else:
            self._tail.next = self.Node(value)
            self._tail = self._tail.next
        self._size += 1

    def dequeue(self):
        if self.empty():
            raise IndexError("Can't dequeue from empty queue")
        ret_node = self._head
        self._head = self._head.next
        ret_node.next = None
        self._size -= 1
        return ret_node.value

    def front(self):
        if self.empty():
            raise IndexError("Can't front from empty queue")
        return self._head.value

    def size(self):
        return self._size

    def empty(self):
        return self._size == 0

    def __iter__(self):
        cur = self._head
        while cur is not None:
            yield cur.value
            cur = cur.next

    def __repr__(self):
        return "LinkedListQueue: front [{}] tail".format('->'.join(str(item) for item in self))


if __name__ == '__main__':
    queue = LinkedListQueue()
    for i in range(10):
        queue.enqueue(i)
        print(queue)
        if i % 3 == 2:
            queue.dequeue()
            print(queue)

    print(queue.front())
    print(queue.size())
