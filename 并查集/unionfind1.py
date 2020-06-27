from unionfind import UF


class UnionFind1(UF):
    def __init__(self, size):
        self.ids = [i for i in range(size)]

    def size(self):
        return len(self.ids)

    def find(self, a):
        return self.ids[a]

    def union(self, a, b):
        aid = self.find(a)
        bid = self.find(b)

        if aid != bid:
            for i, v in enumerate(self.ids):
                if v == aid:
                    self.ids[i] = bid


if __name__ == '__main__':
    size = 20
    uf = UnionFind1(20)

    print(uf.is_connected(0, 1))
    uf.union(0, 1)
    print(uf.is_connected(0, 1))
    uf.union(0, 15)
    print(uf.is_connected(1, 15))
    uf.union(0, 4)
    uf.union(4, 5)
    print(uf.is_connected(4, 15))
    print(uf.is_connected(2, 15))
    print(uf.ids)
