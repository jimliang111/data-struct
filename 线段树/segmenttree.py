class SegmentTree:
    def __init__(self, data, merge):
        self.data = list(data)
        self.tree = [None] * (len(data) * 4)
        self.merge = merge
        self.recursive_render(0, 0, self.size() - 1)

    def left_child(self, i):
        return i * 2 + 1

    def right_child(self, i):
        return i * 2 + 2

    def size(self):
        return len(self.data)

    def recursive_render(self, i, l, r):
        if l == r:
            self.tree[i] = self.data[l]
            return

        middle = (l + r) // 2
        left = self.left_child(i)
        right = self.right_child(i)
        self.recursive_render(left, l, middle)
        self.recursive_render(right, middle + 1, r)

        v = self.merge(self.tree[left], self.tree[right])
        self.tree[i] = v

    def get(self, l, r):
        return self.recursive_get(0, 0, self.size() - 1, l, r)

    def recursive_get(self, i, l_n, r_n, l, r):
        if l_n == l and r_n == r:
            return self.tree[i]

        middle = (l_n + r_n) // 2
        if r <= middle:
            return self.recursive_get(self.left_child(i), l_n, middle, l, r)
        elif middle < l:
            return self.recursive_get(self.right_child(i), middle + 1, r_n, l, r)
        else:
            left = self.recursive_get(
                self.left_child(i), l_n, middle, l, middle)
            right = self.recursive_get(self.right_child(
                i), middle + 1, r_n, middle + 1, r)
            return self.merge(left, right)

    def set(self, index, value):
        self.data[index] = value
        self.recursive_set(0, 0, self.size() - 1, index, value)

    def recursive_set(self, i, l, r, index, value):
        if l == r and l == index:
            self.tree[i] = value
            return

        middle = (l + r) // 2
        left = self.left_child(i)
        right = self.right_child(i)

        if index <= middle:
            self.recursive_set(left, l, middle, index, value)
        else:
            self.recursive_set(right, middle + 1, r, index, value)

        v = self.merge(self.tree[left], self.tree[right])
        self.tree[i] = v

    def __repr__(self):
        return '{!r}'.format(self.tree)


def merge(a, b):
    return a + b


if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    segment_tree = SegmentTree(nums, merge)
    print(segment_tree)

    print(segment_tree.get(2, 5))
    print(segment_tree.get(0, 5))
    print(segment_tree.get(0, 2))

    segment_tree.set(0, -4)
    print(segment_tree)
    print(segment_tree.get(2, 5))
    print(segment_tree.get(0, 5))
    print(segment_tree.get(0, 2))
