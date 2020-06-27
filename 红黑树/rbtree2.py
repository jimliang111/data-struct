RED = True
BLACK = False


class Node:
    def __init__(self, key, value=None, left=None, right=None, p=None, color=RED):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.p = p
        self.color = color

    def __repr__(self):
        return '({}: {})'.format(self.key, self.value)


class RBTree2:

    NIL = Node(None, color=BLACK)

    def __init__(self):
        self.root = self.NIL
        self._size = 0

    def inorder_tree_walk(self, node):
        """ 中序遍历 """
        if node is not self.NIL and node is not None:
            yield from self.inorder_tree_walk(node.left)
            yield node
            yield from self.inorder_tree_walk(node.right)

    def left_rotate(self, x):
        """ 左旋 """
        y = x.right
        x.right = y.left
        if y.left is not self.NIL:
            y.left.p = x
        y.p = x.p

        if x.p is self.NIL:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y

        y.left = x
        x.p = y

    def right_rotate(self, y):
        """ 右旋 """
        x = y.left
        y.left = x.right
        if x.right is not self.NIL:
            x.right.p = y
        x.p = y.p

        if y.p is self.NIL:
            self.root = x
        elif y == y.p.left:
            y.p.left = x
        else:
            y.p.right = x

        x.right = y
        y.p = x

    def get_node(self, x, key):
        node = x
        while node is not self.NIL:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node
        raise KeyError('key do not in RBTree')

    def search(self, node, key):
        return self.get_node(node, key).value

    def minimum(self, node):
        cur = node
        while cur.left is not self.NIL:
            cur = cur.left
        return cur.value

    def maximum(self, node):
        cur = node
        while cur.right is not self.NIL:
            cur = cur.right
        return cur.value

    def successor(self, node):
        cur = node
        if cur.right:
            return self.minimum(self, node.right)
        while cur.p.right is cur and cur.p is not self.NIL:
            cur = cur.p
        if cur.p is self.NIL:
            return None
        return cur.p

    def predecessor(self, node):
        cur = node
        if cur.left:
            return self.maximum(node.left)
        while cur.p.left is cur and cur.p is not self.NIL:
            cur = cur.p
        if cur.p is self.NIL:
            return None
        return cur.p

    def insert(self, key, value=None):
        y = self.NIL
        x = self.root
        while x is not self.NIL:
            y = x
            if key < x.key:
                x = x.left
            elif key > x.key:
                x = x.right
            else:
                x.value = value
                return

        z = Node(key, value, left=self.NIL, right=self.NIL, p=y)
        if y is self.NIL:
            self.root = z
        elif key < y.key:
            y.left = z
        else:
            y.right = z

        self._size += 1
        self.rb_insert_fixup(z)

    def rb_insert_fixup(self, node):
        """ 维持黑平衡 """
        z = node
        while z.p.color == RED:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == RED:
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                    continue
                elif z == z.p.right:
                    z = z.p
                    self.left_rotate(z)

                z.p.color = BLACK
                z.p.p.color = RED
                self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color == RED:
                    z.p.color = BLACK
                    z.p.p.color = RED
                    y.color = BLACK
                    z = z.p.p
                    continue
                elif z == z.p.left:
                    z = z.p
                    self.right_rotate(z)

                z.p.color = BLACK
                z.p.p.color = RED
                self.left_rotate(z.p.p)
        self.root.color = BLACK

    def delete(self, key):
        z = self.get_node(self.root, key)
        y = z
        y_original_color = y.color
        if z.left is self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right is self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        self._size -= 1
        if y_original_color == BLACK:
            self.delete_fixup(x)

    def delete_fixup(self, x):
        while x is not self.root and x.color == BLACK:
            if x == x.p.left:
                w = x.p.right
                if w.color == RED:
                    w.color = BLACK
                    x.p.color = RED
                    self.left_rotate(x.p)
                    w = x.p.right
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.p
                    continue
                elif w.right.color == BLACK:
                    w.left.color = BLACK
                    w.color = RED
                    self.right_rotate(w)
                    w = x.p.right
                w.color = x.p.color
                x.p.color = BLACK
                w.right.color = BLACK
                self.left_rotate(x.p)
                x = self.root
            else:
                w = w.p.left
                if w.color == RED:
                    w.color = BLACK
                    x.p.color = RED
                    self.right_rotate(x.p)
                    w = x.p.left
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.p
                    continue
                elif w.left.color == BLACK:
                    w.right.color = BLACK
                    w.color = RED
                    self.left_rotate(w)
                    w = x.p.left
                w.color = x.p.color
                x.p.color = BLACK
                w.left.color = BLACK
                self.right_rotate(x.p)
                x = self.root
        x.color = BLACK

    def transplant(self, u, v):
        if u.p is self.NIL:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v

        v.p = u.p

    def __len__(self):
        return self._size

    def __contains__(self, key):
        try:
            self.search(self.root, key)
            return True
        except KeyError:
            return False

    def __iter__(self):
        yield from self.inorder_tree_walk(self.root)

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __getitem__(self, key):
        return self.search(self.root, key)

    def __repr__(self):
        return '<RBTree: {}>'.format(','.join(str(item) for item in self))


if __name__ == '__main__':
    bst = RBTree2()
    test_list = [5, 3, 6, 8, 4, 2]
    for i in test_list:
        bst.insert(i)

    print(bst)

    bst.delete(4)
    print(bst)
    bst.delete(6)
    print(bst)

    import fileoperator

    filename = 'pride-and-prejudice.txt'
    total = list(fileoperator.load(filename))

    print(filename)
    print('Total words:', len(total))
    user_map = RBTree2()

    for word in total:
        if word not in user_map:
            user_map[word] = 1
        else:
            user_map[word] += 1

    print('Total different words:', len(user_map))
    print('Frequency of pride:', user_map['pride'])
    print('Frequency of prejudice:', user_map['prejudice'])

    """
    user_map = RBTree2()
    for i in range(2000000):
        user_map[i] = None

    print('finish')
    """
