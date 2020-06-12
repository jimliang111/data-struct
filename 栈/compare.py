import random
import sys
import time
from functools import wraps

from arraystack import ArrayStack
from linkedliststack import LinkedListStack


def timeat(func):
    @wraps(func)
    def wrapper(stack_type, opt_count, stack, *args, **kwargs):
        start = time.time()
        func(stack_type, opt_count, stack, *args, **kwargs)
        end = time.time()
        print('{}, opt_count: {} -> cost {:.6f}s'.format(stack_type,
                                                         opt_count, end - start))
    return wrapper


@timeat
def test_stack(stack_type, opt_count, stack):
    for i in range(opt_count):
        stack.push(random.randint(0, sys.maxsize))
    for i in range(opt_count):
        stack.pop()


if __name__ == '__main__':
    opt_count = 100000

    array_stack = ArrayStack()
    test_stack('Array Stack', opt_count, array_stack)

    linked_list_stack = LinkedListStack()
    test_stack('LinkedList Stack', opt_count, linked_list_stack)
