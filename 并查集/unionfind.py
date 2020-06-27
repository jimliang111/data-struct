import abc


class UF(abc.ABC):

    @abc.abstractmethod
    def size(self):
        """ 并查集大小 """

    @abc.abstractmethod
    def union(self, a, b):
        """ 联合 ab """

    @abc.abstractmethod
    def find(self, a):
        """ 查找并查集中一个元素 """

    def is_connected(self, a, b):
        """ 并查集中两个元素是否连接 """
        return self.find(a) == self.find(b)
