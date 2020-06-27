import abc


class Map(abc.ABC):
	@abc.abstractmethod
	def size(self):
		""" 返回字典大小 """

	@abc.abstractmethod
	def is_empty(self):
		""" 返回字典是否为空 """

	@abc.abstractmethod
	def add(self, k, v):
		""" 新增映射，若k已存在，v覆盖旧值 """

	@abc.abstractmethod
	def get(self, k):
		""" 返回键对应的值 """

	@abc.abstractmethod
	def set(self, k, v):
		""" 设置k对应的新值 """

	@abc.abstractmethod
	def contains(self, k):
		""" 返回 k 是否在映射中 """

	@abc.abstractmethod
	def remove(self, k):
		""" 删除k键，返回它的值 """