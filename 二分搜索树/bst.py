from queue import Queue
import random
import sys


class BST:

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def __repr__(self):
            return str(self.value)

        def __lt__(self, other):
            if self.value < other.value:
                return True
            return False
        """
        def __del__(self):
            # 测试删除节点是否释放内存
            print('del node value {}'.format(self.value))
        """

    def __init__(self):
        self.root = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add(self, e):
        self.root = self.recursive_add(self.root, e)

    def recursive_add(self, node, value):
        """ 递归地添加元素，返回节点 """
        if node is None:
            self._size += 1
            return self.Node(value)

        if value < node.value:
            node.left = self.recursive_add(node.left, value)
        elif value > node.value:
            node.right = self.recursive_add(node.right, value)

        return node

    def contains(self, value):
        return value in self

    def recursive_contains(self, node, value):
        """ 递归地查询元素 """
        if node is None:
            return False

        if node.value == value:
            return True
        elif value < node.value:
            return self.recursive_contains(node.left, value)
        else:
            return self.recursive_contains(node.right, value)

    def min_node(self):
        return self.recursive_min_node(self.root).value

    def recursive_min_node(self, node):
        """ 递归地查找最小的节点，返回节点 """
        if node.left is None:
            return node
        return self.recursive_min_node(node.left)

    def max_node(self):
        return self.recursive_max_node(self.root).value

    def recursive_max_node(self, node):
        """ 递归地查找最大的节点，返回节点 """
        if node.right is None:
            return node
        return self.recursive_max_node(node.right)

    def remove_min(self):
        if self.is_empty():
            raise ValueError('can not remove from empty BST')

        if self.root.left is None:
            ret_node = self.root
            self.root = self.root.right
            self._size -= 1
            return ret_node.value
        else:
            return self.recursive_remove_min(self.root)

    def recursive_remove_min(self, parent):
        """ 递归地查找并删除最小的节点，返回节点的值 """
        if parent.left.left is None:
            ret_node = parent.left
            parent.left = parent.left.right
            self._size -= 1
            return ret_node.value

        return self.recursive_remove_min(parent.left)

    def remove_max(self):
        if self.is_empty():
            raise ValueError('Can not remove from empty BST')

        if self.root.right is None:
            ret_node = self.root
            self.root = self.root.left
            self._size -= 1
            return ret_node.value
        else:
            return self.recursive_remove_max(self.root)

    def recursive_remove_max(self, parent):
        """ 递归地查找并删除最大的节点，返回节点的值 """
        if parent.right.right is None:
            ret_node = parent.right
            parent.right = parent.right.left
            self._size -= 1
            return ret_node.value

        return self.recursive_remove_max(parent.right)

    def remove(self, value):
        if self.is_empty():
            raise ValueError('Can not remove from empty BST')

        self.root = self.recursive_remove(self.root, value)

    def recursive_remove(self, node, value):
        """ 递归地查找并删除指定的节点，无返回值 """
        if node is None:
            raise ValueError('remove fail --> {} do not in BST'.format(value))

        if node.value == value:
            if node.right:
                new_node = node
                if node.right.left:
                    new_node.value = self.recursive_remove_min(node.right)
                else:
                    new_node.value = node.right.value
                    new_node.right = node.right.right
                    self._size -= 1
                return new_node
            else:
                self._size -= 1
                return node.left
        elif value < node.value:
            node.left = self.recursive_remove(node.left, value)
        else:
            node.right = self.recursive_remove(node.right, value)

        return node

    def ergodic(self, mode='front'):
        if mode == 'middle':
            yield from self.recursive_ergodic_middle(self.root)
        elif mode == 'end':
            yield from self.recursive_ergodic_end(self.root)
        elif mode == 'line':
            yield from self.ergodic_line()
        else:
            yield from self.recursive_ergodic_front(self.root)

    def recursive_ergodic_front(self, node):
        """ 前序遍历 """
        if node is None:
            return

        yield node
        yield from self.recursive_ergodic_front(node.left)
        yield from self.recursive_ergodic_front(node.right)

    def recursive_ergodic_middle(self, node):
        """ 中序遍历 """
        if node is None:
            return

        yield from self.recursive_ergodic_middle(node.left)
        yield node
        yield from self.recursive_ergodic_middle(node.right)

    def recursive_ergodic_end(self, node):
        """ 后序遍历 """
        if node is None:
            return

        yield from self.recursive_ergodic_end(node.left)
        yield from self.recursive_ergodic_end(node.right)
        yield node

    def ergodic_line(self):
        """ 层序遍历 """
        q = Queue()
        if self.root is not None:
            q.put(self.root)

        while not q.empty():
            cur = q.get()
            yield cur
            if cur.left:
                q.put(cur.left)
            if cur.right:
                q.put(cur.right)

    def __contains__(self, value):
        return self.recursive_contains(self.root, value)

    def __iter__(self):
        """ 默认为非递归的前序遍历 """
        stack = []
        if self.root is not None:
            stack.append(self.root)

        while stack:
            cur = stack.pop()
            yield cur
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

    def __repr__(self):
        return '<BST: {}>'.format(','.join(str(item) for item in self))


if __name__ == '__main__':
    bst = BST()
    test_list = [5, 3, 6, 8, 4, 2]
    for i in test_list:
        bst.add(i)

    print(bst)

    print(10 in bst)
    print(4 in bst)

    for i in bst.ergodic(mode='line'):
        print(i, end=',')
    print()

    for i in bst.ergodic():
        print(i, end=',')
    print()

    for i in bst.ergodic(mode='middle'):
        print(i, end=',')
    print()

    for i in bst.ergodic(mode='end'):
        print(i, end=',')
    print()

    print(min(bst))
    print(bst.min_node())
    print(max(bst))
    print(bst.max_node())

    print(bst.remove_min())
    print(bst)

    print(bst.remove_max())
    print(bst)
    print(list(bst.ergodic(mode='middle')))

    bst = BST()
    for i in range(1000):
        bst.add(random.randint(0, 1000))

    print(bst.size())
    check = []
    while not bst.is_empty():
        check.append(bst.remove_min())

    if check == sorted(check):
        print('pass')
    else:
        print('error')

    bst = BST()
    for i in range(1000):
        bst.add(random.randint(0, 1000))

    check = []
    while not bst.is_empty():
        check.append(bst.remove_max())

    if check == sorted(check, reverse=True):
        print('pass')
    else:
        print('error')

    bst = BST()

    for i in range(200):
        bst.add(random.randint(0, 999))

    i = 0
    print(bst.size())
    while not bst.is_empty():
        try:
            bst.remove(random.randint(0, 999))
            i += 1
            check = list(bst.ergodic(mode='middle'))
            if check != sorted(check):
                print('fail ---')
                break
        except Exception as e:
            pass
    print(i)
