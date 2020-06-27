class Node:
    def __init__(self, key, value=None, p=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.p = p

    def __repr__(self):
        return '({}: {})'.format(self.key, self.value)


class BST2:
    def __init__(self):
        self.root = None
        self._size = 0

    def inorder_tree_walk(self, node):
        """ 中序遍历 """
        if node is not None:
            yield from self.inorder_tree_walk(node.left)
            yield node
            yield from self.inorder_tree_walk(node.right)

    def tree_serach(self, node, key):
        """ 递归版的搜索 """
        if node is None or node.key == key:
            return node

        if key < node.key:
            return self.tree_serach(node.left, key)
        else:
            return self.tree_serach(node.right, key)

    def iterative_tree_search(self, node, key):
        """ 非递归版的搜索 """
        cur = node
        while cur is not None and key != cur.key:
            if key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        if cur is None:
            raise KeyError('key: {} do not exists'.format(key))
        return cur

    def minimum(self, node):
        """ 最小值 """
        cur = node
        while cur.left:
            cur = cur.left
        return cur

    def maximum(self, node):
        """ 最大值 """
        cur = node
        while cur.right:
            cur = cur.right
        return cur

    def successor(self, node):
        """ 获取后继 """
        if node.right:
            return self.minimum(node.right)
        cur = node
        parent = cur.p
        while parent and cur == parent.right:
            cur = parent
            parent = parent.p
        return parent

    def predecessor(self, node):
        """ 获取前驱 """
        if node.left:
            return self.maximum(node.left)
        cur = node
        parent = node.p
        while parent and cur == parent.left:
            cur = parent
            parent = parent.p
        return parent

    def insert(self, key, value=None):
        """ 添加元素 """
        cur = self.root
        parent = None
        while cur:
            parent = cur
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                cur.value = value
                return
        if parent is None:
            self.root = Node(key, value)
        elif key < parent.key:
            parent.left = Node(key, value, parent)
        else:
            parent.right = Node(key, value, parent)
        self._size += 1

    def delete(self, key):
        """ 删除元素 """
        z = self.iterative_tree_search(self.root, key)
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.p != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
        self._size -= 1
        return z.value

    def transplant(self, u, v):
        if u.p == None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v

        if v:
            v.p = u.p

    def __len__(self):
        return self._size

    def __contains__(self, key):
        try:
            self.iterative_tree_search(self.root, key)
            return True
        except KeyError:
            return False

    def __iter__(self):
        yield from self.inorder_tree_walk(self.root)

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __getitem__(self, key):
        return self.iterative_tree_search(self.root, key).value

    def __repr__(self):
        return '<BST: {}>'.format(','.join(str(item) for item in self))


if __name__ == '__main__':
    bst = BST2()
    test_list = [5, 3, 6, 8, 4, 2]
    for i in test_list:
        bst.insert(i)

    print(bst)

    bst.delete(3)
    print(bst)
