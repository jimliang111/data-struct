"""
letcode 211 添加与搜索单词
涉及一个支持以下两种操作的数据结构：

void addWord(word)
bool search(word)

search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。
示例:
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
"""

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['end'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.recursive_search(self.root, word)

    def recursive_search(self, node, word):
        for i, c in enumerate(word):
            if c != '.':
                if c not in node:
                    return False
                node = node[c]
            else:
                for k in (key for key in node if key != 'end'):
                    if self.recursive_search(node[k], word[i + 1:]):
                        return True
                return False
        return node.get('end', False)
