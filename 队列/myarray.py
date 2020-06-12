from collections.abc import Sequence


class Array:

    def __init__(self, seq=None, capacity=10):
        if seq:
            if not isinstance(seq, Sequence):
                raise TypeError('seq must a sequece')
            self._data = list(seq) + [None] * len(seq)
            self._size = len(seq)
        else:
            self._data = [None] * capacity
            self._size = 0

    def get_size(self):
        # 获取数组的元素个数
        return self._size

    def get_capacity(self):
        # 获取数组容量
        return len(self._data)

    def is_empty(self):
        # 数组是否为空
        return len(self._size) == 0

    def add_last(self, e):
        self.add(self._size, e)

    def add_first(self, e):
        self.add(0, e)

    def add(self, index, e):
        self._check_index(index)

        if (self._size == len(self._data)):
            self._resize(2 * len(self._data))

        for i in range(self._size - 1, index - 1, -1):
            self._data[i + 1] = self._data[i]

        self._data[index] = e
        self._size += 1

    def get(self, index):
        self._check_index(index)
        return self._data[index]

    def get_last(self):
        return self.get(self._size - 1)

    def get_first(self):
        return self.get(0)

    def set(self, index, e):
        self._check_index(index)
        self._data[index] = e

    def contains(self, e):
        """
        return e in self._data
        """
        for item in self._data:
            if item == e:
                return True
        return False

    def find(self, e):
        """
        try:
            return self._data.index(e)
        except ValueError:
            return -1
        """
        for i in range(self._size):
            if self._data[i] == e:
                return i
        return -1

    def remove(self, index):
        self._check_index(index)
        ret = self._data[index]
        for i in range(index + 1, self._size):
            self._data[i - 1] = self._data[i]
        self._size -= 1

        if self._size == len(self._data) // 4 and len(self._data) // 2 != 0:
            self._resize(len(self._data) // 2)
        return ret

    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self._size - 1)

    def remove_element(self, e):
        i = self.find(e)
        if i != -1:
            self.remove(i)

    def _resize(self, new_capacity):
        new_arr = [None] * new_capacity
        for i in range(self._size):
            new_arr[i] = self._data[i]
        self._data = new_arr

    def _check_index(self, index):
        cls = type(self)
        if not isinstance(index, int):
            raise TypeError(f'{cls.__name__} index must interger')

        if (index < 0 or index > self._size):
            raise ValueError(
                f'{cls.__name__} require index >= 0 and <= self.size')

    def __getitem__(self, index):
        self._check_index(index)
        return self._data[index]

    def __len__(self):
        return self._size

    def __iter__(self):
        for i in range(self._size):
            yield self._data[i]

    def __repr__(self):
        return f"Array: size = {self._size}, capacity = {self.get_capacity()}\n[ {', '.join(str(item) for item in self)} ]"


def main():
    arr = Array()
    for i in range(10):
        arr.add_last(i)
    print(arr)
    arr.add(1, 100)
    print(arr)
    arr.add_first(-1)
    print(arr)
    print(arr.contains(-1))
    print(arr.contains(999))
    print(arr.find(100))
    print(arr.find(999))
    arr.remove(2)
    print(arr)
    arr.remove_element(4)
    print(arr)
    arr.remove_first()
    print(arr)
    print(arr[3])
    print(len(arr))
    for item in arr:
        print(item)
    # print(arr['2'])
    arr2 = Array([1, 2, 3])
    print(arr2)
    arr3 = Array('abc')
    print(arr3)
    arr4 = Array((1, 2, 3))
    print(arr4)
    arr5 = Array(i for i in range(10))
    print(arr5)


if __name__ == '__main__':
    main()
