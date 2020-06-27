class Trie:
    class Node:
        def __init__(self, is_word=False):
            self.is_word = is_word
            self.next = dict()

    def __init__(self):
        self.root = self.Node()
        self._size = 0

    def add(self, word):
        cur = self.root
        for c in word:
            if not cur.next.get(c):
                cur.next[c] = self.Node()
            cur = cur.next.get(c)
        if not cur.is_word:
            cur.is_word = True
            self._size += 1

    def contains(self, word):
        cur = self.root
        for c in word:
            if not cur.next.get(c):
                return False
            cur = cur.next.get(c)
        return cur.is_word

    def prefix(self, word):
        cur = self.root
        for c in word:
            if not cur.next.get(c):
                return False
            cur = cur.next.get(c)
        return True

    def size(self):
        return self._size
