import abc


class Queue(abc.ABC):

    @abc.abstractmethod
    def enqueue(e):
        """ 添加元素 """

    @abc.abstractmethod
    def dequeue():
        """ 取出元素 """

    @abc.abstractmethod
    def front():
        """ 查看队列头部元素 """

    @abc.abstractmethod
    def size():
        """ 队列大小 """

    @abc.abstractmethod
    def empty():
        """ 是否为空 """
