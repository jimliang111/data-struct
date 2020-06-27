from map import Map


class LinkedListMap(Map):

    class Node:
        def __init__(self, k=None, v=None, next_node=None):
            self._key = k
            self._value = v
            self._next = next_node

        def __repr__(self):
            return '({!r}, {!r})'.format(self._key, self._value)

    def __init__(self):
        self.__dummy_head = self.Node()
        self.__size = 0

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def add(self, k, v):
        self[k] = v

    def get(self, k):
        return self[k]

    def contains(self, k):
        return k in self

    def set(self, k, v):
        node = self._get_node(k)
        node._value = v

    def remove(self, key):
        prev = self.__dummy_head
        while prev._next:
            if prev._next._key == key:
                ret = prev._next
                prev._next = prev._next._next
                self.__size -= 1
                return ret._value
            prev = prev._next
        raise KeyError('Key {} does not exists'.format(key))

    def _get_node(self, key):
        for item in self:
            if item._key == key:
                return item
        raise KeyError('Key {} does not exists'.format(key))

    def __len__(self):
        return self.__size

    def __getitem__(self, key):
        return self._get_node(key)._value

    def __setitem__(self, key, value):
        try:
            node = self._get_node(key)
            node._value = value
        except KeyError:
            self.__dummy_head._next = self.Node(
                key, value, self.__dummy_head._next)
            self.__size += 1

    def __contains__(self, k):
        for item in self:
            if item._key == k:
                return True
        return False

    def __iter__(self):
        cur = self.__dummy_head._next
        while cur:
            yield cur
            cur = cur._next

    def __repr__(self):
        return '<LinkedListMap: {!r}>'.format(','.join(str(item) for item in self))


if __name__ == '__main__':
    """
    user_map = LinkedListMap()
    for i in range(10):
        user_map.add(i, i)

    print(user_map)

    user_map[9] = 8
    print(user_map)

    user_map[10] = 10
    print(user_map)

    print(user_map[10])

    user_map.remove(2)
    print(user_map)

    print(len(user_map))
    """
    import fileoperator

    filename = 'pride-and-prejudice.txt'
    total = list(fileoperator.load(filename))

    print(filename)
    print('Total words:', len(total))
    user_map = LinkedListMap()

    for word in total:
        if word not in user_map:
            user_map[word] = 0
        user_map[word] += 1

    print('Total different words:', len(user_map))
    print('Frequency of pride:', user_map['pride'])
    print('Frequency of prejudice:', user_map['prejudice'])
