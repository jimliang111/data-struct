class RBTree:
    RED = True
    BLACK = False

    class Node:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.color = RBTree.RED

        def __repr__(self):
            return '({}, {})'.format(self.key, self.value)

    def __init__(self):
        self.root = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def get_node(self, node, key):
        if node is None:
            raise KeyError('key {} do not in RBTree')

        if key < node.key:
            return self.get_node(node.left, key)
        elif key > node.key:
            return self.get_node(node.right, key)
        else:
            return node

    def get(self, key):
        return self.get_node(self.root, key).value

    def contains(self, key):
        try:
            self.get_node(self.root, key)
            return True
        except KeyError:
            return False

    def ergodic_middle(self, node):
        if node:
            yield from self.ergodic_middle(node.left)
            yield node
            yield from self.ergodic_middle(node.right)

    def is_red(self, node):
        if node is None:
            return False
        return node.color

    def add(self, key, value=None):
        self.root = self.recursive_add(self.root, key, value)
        self.root.color = self.BLACK

    def recursive_add(self, node, key, value):
        if node is None:
            self._size += 1
            return self.Node(key, value)

        if key < node.key:
            node.left = self.recursive_add(node.left, key, value)
        elif key > node.key:
            node.right = self.recursive_add(node.right, key, value)
        else:
            node.value = value

        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.left_rotate(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.right_rotate(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)

        return node

    def left_rotate(self, node):
        x = node.right
        node.right = x.left
        x.left = node

        x.color = node.color
        node.color = self.RED

        return x

    def right_rotate(self, node):
        x = node.left
        node.left = x.right
        x.right = node

        x.color = node.color
        node.color = self.RED

        return x

    def flip_colors(self, node):
        node.color = self.RED
        node.left.color = self.BLACK
        node.right.color = self.BLACK

    def __len__(self):
        return self._size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.add(key, value)

    def __contains__(self, key):
        return self.contains(key)

    def __iter__(self):
        yield from self.ergodic_middle(self.root)

    def __str__(self):
        return "RBTree ({})".format(', '.join(str(item) for item in self))


if __name__ == '__main__':
    import fileoperator

    filename = 'pride-and-prejudice.txt'
    total = list(fileoperator.load(filename))

    print(filename)
    print('Total words:', len(total))
    user_map = RBTree()

    for word in total:
        if word not in user_map:
            user_map[word] = 0
        user_map[word] += 1

    print('Total different words:', len(user_map))
    print('Frequency of pride:', user_map['pride'])
    print('Frequency of prejudice:', user_map['prejudice'])
