import time
import random
import sys

from arrayqueue import ArrayQueue
from loopqueue import LoopQueue
from linkedlistqueue import LinkedListQueue


def test_query(q, count):
    t1 = time.time()
    for i in range(count):
        q.enqueue(random.randint(0, sys.maxsize))
    for i in range(count):
        q.dequeue()
    t2 = time.time() - t1
    return t2


if __name__ == '__main__':
    array_queue = ArrayQueue()
    loop_queue = LoopQueue()
    linked_queue = LinkedListQueue()

    count = 1000000

    # t1 = test_query(array_queue, count)
    t2 = test_query(loop_queue, count)
    t3 = test_query(linked_queue, count)

    # print(f'array queue time: {t1:.6f}s')
    print(f'loop queue time: {t2:.6f}s')
    print(f'linked_list queue time: {t3:.6f}s')
