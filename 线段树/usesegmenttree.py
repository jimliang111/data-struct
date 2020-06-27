"""
leetcode 307
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
update(i, val) 函数可以通过将下标为 i 的数值更新为 val，从而对数列进行修改。

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
"""

class NumArray:

    def __init__(self, nums: List[int]):
        self.data = nums
        self.tree = [None] * (len(nums) * 4)
        if len(nums):
            self.render(0, 0, len(self.data) - 1)

    def update(self, i: int, val: int) -> None:
        self.data[i] = val
        self.recursive_set(0, 0, len(self.data) - 1, i, val)

    def sumRange(self, i: int, j: int) -> int:
        return self.recursive_get(0, 0, self.size() - 1, i, j)

    def render(self, i, l, r):
        if l == r:
            self.tree[i] = self.data[l]
            return

        middle = (l + r) // 2
        left = self.left_child(i)
        right = self.right_child(i)
        self.render(left, l, middle)
        self.render(right, middle + 1, r)

        v = self.merge(self.tree[left], self.tree[right])
        self.tree[i] = v

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

    def left_child(self, i):
        return i * 2 + 1

    def right_child(self, i):
        return i * 2 + 2

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

    def merge(self, a, b):
        return a + b

    def size(self):
        return len(self.data)
