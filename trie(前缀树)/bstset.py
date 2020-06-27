from bst import BST
from userset import UserSet
import fileoperator


class BSTSet(UserSet):
    def __init__(self):
        self._bst = BST()

    def size(self):
        return self._bst.size()

    def is_empty(self):
        return self._bst.is_empty()

    def add(self, item):
        self._bst.add(item)

    def remove(self, item):
        self._bst.remove(item)

    def contains(self, item):
        return item in self._bst


if __name__ == '__main__':
    filename = 'pride-and-prejudice.txt'
    total = list(fileoperator.load(filename))

    print(len(total))

    bst_set = BSTSet()
    for i in total:
        bst_set.add(i)

    print('undifference word:', bst_set.size())
