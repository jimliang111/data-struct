from myarray import Array
from stack import Stack


class ArrayStack(Stack):

    def __init__(self, seq=None, capacity=10):
        self._array = Array(seq, capacity)

    def peek(self):
        return self._array.get_last()

    def push(self, e):
        self._array.add_last(e)

    def pop(self):
        return self._array.remove_last()

    def empty(self):
        return self._array.is_empty()

    def size(self):
        return self._array.get_size()

    def capacity(self):
        return self._array.get_capacity()

    def __repr__(self):
        return f"{self.__class__.__name__}: [ {'. '.join(str(item) for item in self._array)} ] top"


if __name__ == '__main__':
    stack = ArrayStack()
    for i in range(5):
        stack.push(i)
        print(stack)
    stack.pop()
    print(stack)
