class AVLTree:

    class Node:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.height = 1

        def __repr__(self):
            return '({}: {})'.format(self.key, self.value)

    def __init__(self):
        self.root = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def contains(self, key):
        try:
            self.get_node(self.root, key)
            return True
        except KeyError:
            return False

    def get_node(self, node, key):
        if node is None:
            raise KeyError('key: {} do not in AVLTree'.format(key))

        if key < node.key:
            return self.get_node(node.left, key)
        elif key > node.key:
            return self.get_node(node.right, key)
        else:
            return node

    def get(self, key):
        return self.get_node(self.root, key).value

    def add(self, key, value=None):
        self.root = self.recursive_add(self.root, key, value)

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

        self.node_set_height(node)

        node = self.keep_balance(node)

        return node

    def remove(self, key):
        node_value = self.get(key)
        self.root = self.recursive_remove(self.root, key)
        return node_value

    def recursive_remove(self, node, key):
        if node.key == key:
            if not node.right:
                self._size -= 1
                node = node.left
            else:
                min_node = self.min_node(node.right)
                new_node = self.Node(min_node.key, min_node.value)
                new_node.left = node.left
                new_node.right = self.recursive_remove(
                    node.right, min_node.key)
                node = new_node
        elif key < node.key:
            node.left = self.recursive_remove(node.left, key)
        else:
            node.right = self.recursive_remove(node.right, key)

        self.node_set_height(node)

        node = self.keep_balance(node)

        return node

    def min_node(self, node):
        if node.left is None:
            return node

        return self.min_node(node.left)

    def keep_balance(self, node):
        balance_factor = self.node_balance_factor(node)

        if balance_factor > 1 and self.node_balance_factor(node.left) >= 0:
            return self.rotate_right(node)
        elif balance_factor > 1 and self.node_balance_factor(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        elif balance_factor < -1 and self.node_balance_factor(node.right) <= 0:
            return self.rotate_left(node)
        elif balance_factor < -1 and self.node_balance_factor(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def node_height(self, node):
        if node is None:
            return 0
        return node.height

    def node_set_height(self, node):
        if node is None:
            return

        node.height = max(self.node_height(node.left),
                          self.node_height(node.right)) + 1

    def node_balance_factor(self, node):
        if node is None:
            return 0
        return self.node_height(node.left) - self.node_height(node.right)

    def rotate_right(self, node):
        head = node.left
        head_r = head.right
        node.left = head_r
        head.right = node

        self.node_set_height(node)
        self.node_set_height(head)
        return head

    def rotate_left(self, node):
        head = node.right
        head_l = head.left
        node.right = head_l
        head.left = node

        self.node_set_height(node)
        self.node_set_height(head)
        return head

    def is_avl_tree(self):
        return self.recursive_is_avl_tree(self.root)

    def recursive_is_avl_tree(self, node):
        if node is None:
            return True

        if abs(self.node_balance_factor(node)) > 1:
            # print(abs(self.node_balance_factor(node)))
            return False

        return self.recursive_is_avl_tree(node.left) and self.recursive_is_avl_tree(node.right)

    def is_bst(self):
        order_list = [item.key for item in self]
        for i in range(1, len(order_list)):
            if order_list[i] < order_list[i - 1]:
                return False
        return True

    def ergodic_middle(self, node):
        if node:
            yield from self.ergodic_middle(node.left)
            yield node
            yield from self.ergodic_middle(node.right)

    def __iter__(self):
        yield from self.ergodic_middle(self.root)

    def __setitem__(self, key, value):
        self.add(key, value)

    def __len__(self):
        return self.size()

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return self.contains(key)

    def __repr__(self):
        return "AVLTree ({})".format(', '.join(str(item) for item in self))


if __name__ == '__main__':

    user_map = AVLTree()
    for i in range(10):
        user_map.add(i)
    print('avltree size:', user_map.size())
    print('is Balanced:', user_map.is_avl_tree())
    print('is BST:', user_map.is_bst())

    user_map.remove(0)
    user_map.remove(1)

    print('avltree size:', user_map.size())
    print('is Balanced:', user_map.is_avl_tree())
    print('is BST:', user_map.is_bst())

    import fileoperator

    filename = 'pride-and-prejudice.txt'
    total = list(fileoperator.load(filename))

    print(filename)
    print('Total words:', len(total))
    user_map = AVLTree()

    for word in total:
        if word not in user_map:
            user_map[word] = 0
        user_map[word] += 1

    print('Total different words:', len(user_map))
    print('Frequency of pride:', user_map['pride'])
    print('Frequency of prejudice:', user_map['prejudice'])
    print('is Balanced:', user_map.is_avl_tree())
    print('is BST:', user_map.is_bst())

    for word in total:
        if word in user_map:
            user_map.remove(word)
            if not user_map.is_bst() or not user_map.is_avl_tree():
                raise RuntimeError('error')

    print('avltree size:', user_map.size())
