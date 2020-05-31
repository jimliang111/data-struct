import abc


class Stack(abc.ABC):

    @abc.abstractmethod
    def push(e):
        """入栈"""

    @abc.abstractmethod
    def pop():
        """出栈"""

    @abc.abstractmethod
    def peek():
        """查看栈顶元素"""

    @abc.abstractmethod
    def empty():
        """是否为空"""

    @abc.abstractmethod
    def size():
        """返回栈的长度"""
