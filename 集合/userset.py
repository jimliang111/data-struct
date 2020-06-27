import abc


class UserSet(abc.ABC):
    @abc.abstractmethod
    def add(self, item):
        """ 添加元素 """

    @abc.abstractmethod
    def remove(self, item):
        """ 删除元素 """

    @abc.abstractmethod
    def contains(self, item):
        """ 是否存在 """

    @abc.abstractmethod
    def size(self):
        """ 集合大小 """

    @abc.abstractmethod
    def is_empty(self):
        """ 集合是否为空 """
