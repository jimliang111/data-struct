from map import Map


class BSTMap(Map):

    class Node:
        def __init__(self, key, value, left=None, right=None):
            self._key = key
            self.value = value
            self.left = left
            self.right = right

        def __repr__(self):
            return '({!r}, {!r})'.format(self._key, self.value)

    def __init__(self):
        self.root = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add(self, key, value):
        self.root = self.recursive_add(self.root, key, value)

    def recursive_add(self, node, key, value):
        if node is None:
            self._size += 1
            return self.Node(key, value)

        if key < node._key:
            node.left = self.recursive_add(node.left, key, value)
        elif key > node._key:
            node.right = self.recursive_add(node.right, key, value)
        else:
            node.value = value

        return node

    def _get_node(self, key):
        return self._recursive_get_node(self.root, key)

    def _recursive_get_node(self, node, key):
        if node is None:
            raise KeyError('key {} does not exists'.format(key))

        if key < node._key:
            return self._recursive_get_node(node.left, key)
        elif key > node._key:
            return self._recursive_get_node(node.right, key)
        else:
            return node

    def contains(self, key):
        try:
            self._get_node(key)
            return True
        except KeyError:
            return False

    def get(self, key):
        return self._get_node(key).value

    def set(self, key, value):
        node = self._get_node(key)
        node.value = value

    def remove(self, key):
        del_node = self._get_node(key)
        self.root = self.recursive_remove(self.root, key)
        return del_node.value

    def recursive_remove(self, node, key):

        if key < node._key:
            node.left = self.recursive_remove(node.left, key)
        elif key > node._key:
            node.right = self.recursive_remove(node.right, key)
        else:
            if node.right is None:
                self._size -= 1
                return node.left
            else:
                successor = self.recursive_get_min(node.right)
                node.value = successor.value
                node._key = successor._key
                node.right = self.recursive_remove_min(node.right)
        return node

    def recursive_remove_min(self, node):

        if node is None:
            return None

        if node.left is None:
            self._size -= 1
            return node.right
        else:
            node.left = self.recursive_remove_min(node.left)

        return node

    def recursive_get_min(self, node):
        if node.left is None:
            return node
        return self.recursive_get_min(node.left)

    def recursive_ergodic_middle(self, node):
        if node:
            yield from self.recursive_ergodic_middle(node.left)
            yield node
            yield from self.recursive_ergodic_middle(node.right)

    def __iter__(self):
        yield from self.recursive_ergodic_middle(self.root)

    def __len__(self):
        return self._size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.add(key, value)

    def __contains__(self, key):
        return self.contains(key)

    def __repr__(self):
        return "BST ({})".format(', '.join(str(item) for item in self))


if __name__ == '__main__':
    """
    bst = BSTMap()
    test_list = [5, 3, 6, 8, 4, 2]
    for i in test_list:
        bst.add(i, i)

    print(bst)
    print(bst[6])
    bst[6] = 66
    print(bst)

    bst.remove(3)
    print(bst)

    bst[9] = 99
    print(bst)

    bst[9] += 1
    print(bst)

    bst.remove(6)
    print(bst)

    print(bst.size())
    """

    import fileoperator

    filename = 'pride-and-prejudice.txt'
    total = list(fileoperator.load(filename))

    print(filename)
    print('Total words:', len(total))
    user_map = BSTMap()

    for word in total:
        if word not in user_map:
            user_map[word] = 0
        user_map[word] += 1

    print('Total different words:', len(user_map))
    print('Frequency of pride:', user_map['pride'])
    print('Frequency of prejudice:', user_map['prejudice'])
