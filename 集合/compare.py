import time
from functools import wraps

from linkedlistset import LinkedListSet
from bstset import BSTSet
from userset import UserSet
import fileoperator


def timeat(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return end - start
    return wrapper


@timeat
def test_set(the_set, total):
    for item in total:
        the_set.add(item)
    size = the_set.size() if isinstance(the_set, UserSet) else len(the_set)
    print('Total different words:', size)


if __name__ == '__main__':
    filename = 'pride-and-prejudice.txt'
    total = list(fileoperator.load(filename))

    print(filename)
    print('Total words:', len(total))
    bst_set = BSTSet()
    cost1 = test_set(bst_set, total)
    print('BST Set: {:.6f}s'.format(cost1))

    print()

    print(filename)
    print('Total words:', len(total))
    build_in_set = set()
    cost2 = test_set(build_in_set, total)
    print('build_in Set: {:.6f}s'.format(cost2))

    print()

    print(filename)
    print('Total words:', len(total))
    linked_list_set = LinkedListSet()
    cost3 = test_set(linked_list_set, total)
    print('LinkedList Set: {:.6f}s'.format(cost3))
