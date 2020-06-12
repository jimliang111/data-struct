class LinkedList:

    class Node:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next = next_node

        def __repr__(self):
            return str(self.value)

    def __init__(self):
        self._dummy_head = self.Node(None)
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add(self, value, index):
        if index < 0 or index > self._size:
            raise IndexError('index must be >=0 and <= self.get_size()')
        prev = self._dummy_head
        for i in range(index):
            prev = prev.next
        prev.next = self.Node(value, prev.next)
        self._size += 1

    def add_first(self, value):
        self.add(value, 0)

    def add_last(self, value):
        self.add(value, self._size)

    def get(self, index):
        return self[index].value

    def get_first(self):
        return self[0].value

    def get_last(self):
        return self[self._size]

    def set(self, value, index):
        self[index].value = value

    def remove(self, index):
        if index < 0 or index >= self._size:
            raise IndexError('index must be >=0 and < self.get_size()')
        prev = self._dummy_head
        for i in range(index):
            prev = prev.next
        ret_node = prev.next
        prev.next = ret_node.next
        ret_node.next = None
        self._size -= 1
        return ret_node.value

    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self._size - 1)

    def contains(self, value):
        return value in self

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if self.is_empty():
            raise IndexError("can't get from an empty linked_list")
        if index < 0 or index >= self._size:
            raise IndexError('index must be >=0 and < self.get_size()')
        cur = self._dummy_head.next
        for i in range(index):
            cur = cur.next
        return cur

    def __iter__(self):
        cur = self._dummy_head.next
        while cur is not None:
            yield cur.value
            cur = cur.next

    def __repr__(self):
        return 'linked_list: {}->None'.format('->'.join(str(item) for item in self))


if __name__ == '__main__':
    linked_list = LinkedList()
    for i in range(10):
        linked_list.add_first(i)
        print(linked_list)

    linked_list.add(666, 2)
    print(linked_list)

    linked_list.set(66, 2)
    print(linked_list)

    linked_list.remove_last()
    print(linked_list)

    linked_list.remove_first()
    print(linked_list)

    linked_list.add_last(999)
    print(linked_list)

    print(len(linked_list))
    print(linked_list[0])
    print(linked_list.contains(999))
    print(linked_list.contains(9999))

    for i in linked_list:
        print(i, end='->')
