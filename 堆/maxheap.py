from userarray import Array


class MaxHeap:
    def __init__(self):
        self._arr = Array()

    def size(self):
        return self._arr.get_size()

    def is_empty(self):
        return self._arr.is_empty()

    def _parent(self, i):
        if i == 0:
            raise IndexError('Can not get parent from root')
        return (i - 1) // 2

    def _left_child(self, i):
        return i * 2 + 1

    def _right_child(self, i):
        return i * 2 + 2

    def add(self, item):
        self._arr.add_last(item)
        self.shift_up(self.size() - 1)

    def shift_up(self, i):
        while i > 0:
            p = self._parent(i)
            if self._arr[i] > self._arr[p]:
                self._arr[i], self._arr[p] = self._arr[p], self._arr[i]
            i = p

    def pop_max(self):
        pop_item = self._arr.get_first()
        last_item = self._arr.remove_last()
        self._arr.set(0, last_item)
        self.shift_down(0)
        return pop_item

    def see_max(self):
        return self._arr[0]

    def shift_down(self, i):
        while self._left_child(i) < self.size():
            l, r = self._left_child(i), self._right_child(i)

            temp_l = (i, l, r) if r < self.size() else (i, l)
            temp_d = {self._arr[index]: index for index in temp_l}
            max_v = max(temp_d)
            if max_v == self._arr[i]:
                break
            else:
                self._arr[i], self._arr[temp_d[max_v]
                                        ] = self._arr[temp_d[max_v]], self._arr[i]
                i = temp_d[max_v]

    def contains(self, item):
        return item in self._arr

    def replace(self, item):
        ret = self._arr[0]
        self._arr[0] = item
        self.shift_down(0)
        return ret

    @classmethod
    def heapify(cls, iterable):
        arr = Array(iterable)
        obj = cls()
        obj._arr = arr
        i = obj._parent(arr.get_size() - 1)
        while i >= 0:
            obj.shift_down(i)
            i -= 1
        return obj

    def __len__(self):
        return len(self._arr)

    def __iter__(self):
        return iter(self._arr)

    def __repr__(self):
        return str(self._arr)

    def __getitem__(self, index):
        return self._arr[index]


if __name__ == '__main__':
    import random
    import sys

    heap = MaxHeap()
    for i in range(100):
        heap.add(random.randint(0, sys.maxsize))

    l = []

    for i in range(100):
        l.append(heap.pop_max())

    for i in range(1, len(l)):
        if l[i - 1] < l[i]:
            raise ValueError('error')

    beap = MaxHeap.heapify([random.randint(0, 1000) for i in range(20)])
    print(beap)

    print(beap.replace(66))
    print(beap)

    print('max heap test complated')
