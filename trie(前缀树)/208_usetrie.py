"""
letcode 208 实现 Trie
实现一个 Trie，包含 insert，search，startswtih 这个三个操作

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true
"""

class Trie:

    class Node:
        def __init__(self, is_word=False):
            self.is_word = is_word
            self.next = dict()

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for c in word:
            if not cur.next.get(c):
                cur.next[c] = self.Node()
            cur = cur.next.get(c)

        if not cur.is_word:
            cur.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for c in word:
            if not cur.next.get(c):
                return False
            cur = cur.next.get(c)
        return cur.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for c in prefix:
            if not cur.next.get(c):
                return False
            cur = cur.next.get(c)
        return True
