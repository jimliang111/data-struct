class HashTable:
    CAPACITY = [53, 97, 193, 389, 769, 1543, 3079, 6151, 12289, 24593, 49157, 98317, 196613, 393241, 786433, 1572869,
                3145739, 6291469, 12582917, 25165843, 50331653, 100663319, 201326611, 402653189, 805306457, 1610612741]

    MAX_FERR_ADD = 0.67
    MAX_FERR_SUB = 0.5

    class LinkedList:
        def __init__(self, key, value=None, next_node=None):
            self.key = key
            self.value = value
            self.next = next_node

        def __repr__(self):
            return '({}: {})'.format(self.key, self.value)

    def __init__(self):
        self._size = 0
        self.capacity_index = 0
        self.hash_table = [self.LinkedList(None) for i in range(
            self.CAPACITY[self.capacity_index])]

    def hash_key(self, key):
        return (hash(key) & 0x7fffffff) % self.CAPACITY[self.capacity_index]

    def add(self, key, value=None):
        node = self.hash_table[self.hash_key(key)]

        while node:
            if node.next is None:
                self._size += 1
                node.next = self.LinkedList(key, value)
                break

            if node.next.key == key:
                node.next.value = value
                break
            node = node.next

        if self._size >= self.CAPACITY[self.capacity_index] * self.MAX_FERR_ADD:
            self.resize(self.capacity_index + 1)

    def remove(self, key):
        hash_key = self.hash_key(key)
        node = self.hash_table[hash_key]

        while node.next:
            if node.next is None:
                raise KeyError('Key: {} do not in HashTable'.format(key))

            if node.next.key == key:
                ret_node = node.next
                node.next = ret_node.next
                ret_node.next = None
                self._size -= 1
                return ret_node.value
            node = node.next

        if self._size <= self.CAPACITY[self.capacity_index] * self.MAX_FERR_SUB:
            self.resize(self.capacity_index - 1)

    def get(self, key):
        hash_key = self.hash_key(key)
        node = self.hash_table[hash_key].next

        while node:
            if node.key == key:
                return node
            node = node.next
        raise KeyError('Key: {} do not in HashTable'.format(key))

    def resize(self, index):
        self.capacity_index = index
        new_hash_table = [self.LinkedList(None) for i in range(
            self.CAPACITY[self.capacity_index])]

        for item in self:
            head = new_hash_table[self.hash_key(item.key)]
            while head.next:
                head = head.next
            head.next = self.LinkedList(item.key, item.value)

        self.hash_table = new_hash_table

    def contains(self, key):
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def __getitem__(self, key):
        return self.get(key).value

    def __setitem__(self, key, value):
        self.add(key, value)

    def __contains__(self, key):
        return self.contains(key)

    def __len__(self):
        return self._size

    def __iter__(self):
        for node in self.hash_table:
            node = node.next
            while node:
                yield node
                node = node.next


if __name__ == '__main__':
    user_map = HashTable()

    for i in range(57):
        user_map.add(i, i)

    print(len(user_map))

    user_map.remove(2)
    user_map.remove(4)

    for item in user_map:
        print(item)

    print(len(user_map))

    import fileoperator

    filename = 'pride-and-prejudice.txt'
    total = list(fileoperator.load(filename))

    print(filename)
    print('Total words:', len(total))
    user_map = HashTable()

    for word in total:
        if word not in user_map:
            user_map[word] = 1
        else:
            user_map[word] += 1

    print('Total different words:', len(user_map))
    print('Frequency of pride:', user_map['pride'])
    print('Frequency of prejudice:', user_map['prejudice'])
