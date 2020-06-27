import time
import random
from unionfind1 import UnionFind1
from unionfind2 import UnionFind2


def test_union_find(numbers, times, uf):
    start = time.time()

    for i in range(times):
        a = random.randint(0, numbers - 1)
        b = random.randint(0, numbers - 1)
        uf.union(a, b)
    for i in range(times):
        a = random.randint(0, numbers - 1)
        b = random.randint(0, numbers - 1)
        uf.is_connected(a, b)

    return time.time() - start


if __name__ == '__main__':
    numbers = 10000000
    times = 10000000

    # uf1 = UnionFind1(numbers)
    uf2 = UnionFind2(numbers)

    # t1 = test_union_find(numbers, times, uf1)
    # print('uf1: {:.6f}'.format(t1))

    t2 = test_union_find(numbers, times, uf2)
    print('uf2: {:.6f}'.format(t2))
