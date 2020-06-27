from linkedlist import LinkedList
from userset import UserSet
import fileoperator


class LinkedListSet(UserSet):

    def __init__(self):
        self._linkedlist = LinkedList()

    def size(self):
        return self._linkedlist.get_size()

    def is_empty(self):
        return self._linkedlist.is_empty()

    def add(self, item):
        if not self._linkedlist.contains(item):
            self._linkedlist.add_first(item)

    def remove(self, item):
        self._linkedlist.remove_value(item)

    def contains(self, value):
        return self._linkedlist.contains(value)


if __name__ == '__main__':
    filename = 'pride-and-prejudice.txt'
    total = list(fileoperator.load(filename))

    print(len(total))

    bst_set = LinkedListSet()
    for i in total:
        bst_set.add(i)

    print('undifference word:', bst_set.size())
