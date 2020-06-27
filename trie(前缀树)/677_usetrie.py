"""
leetcode 677 键值映射
实现一个 MapSum 类里的两个方法，insert 和 sum。
对于方法 insert，你将得到一对（字符串，整数）的键值对。字符串表示键，整数表示值。如果键已经存在，那么原来的键值对将被替代成新的键值对。
对于方法 sum，你将得到一个表示前缀的字符串，你需要返回所有以该前缀开头的键的值的总和。

示例 1:
输入: insert("apple", 3), 输出: Null
输入: sum("ap"), 输出: 3
输入: insert("app", 2), 输出: Null
输入: sum("ap"), 输出: 5
"""

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for k in key:
            cur = cur.setdefault(k, {})
        cur['v'] = val

    def sum(self, prefix: str) -> int:
        cur = self.root
        for k in prefix:
            if k not in cur:
                return 0
            cur = cur[k]
        return self.recursive_sum(cur)

    def recursive_sum(self, node):
        value = node.get('v', 0)
        for k in (key for key in node if key != 'v'):
            value += self.recursive_sum(node[k])
        return value
