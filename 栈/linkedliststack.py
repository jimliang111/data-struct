from stack import Stack
from linkedlist import LinkedList


class LinkedListStack(Stack):
    """
    基于链表的栈
    """

    def __init__(self):
        self._linked_list = LinkedList()

    def peek(self):
        return self._linked_list.get_first()

    def push(self, value):
        self._linked_list.add_first(value)

    def pop(self):
        return self._linked_list.remove_first()

    def empty(self):
        return self._linked_list.is_empty()

    def size(self):
        return self._linked_list.get_size()

    def __repr__(self):
        return f"{self.__class__.__name__}: top [ {'->'.join(str(item) for item in self._linked_list)} ]"


if __name__ == '__main__':
    stack = LinkedListStack()
    for i in range(5):
        stack.push(i)
        print(stack)
    stack.pop()
    print(stack)
