from unionfind import UF


class UnionFind2(UF):
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.ranks = [1 for i in range(size)]

    def size(self):
        return len(self.parents)

    def find(self, a):
        return self.recursive_find(a)

    def recursive_find(self, i):
        if i != self.parents[i]:
            self.parents[i] = self.recursive_find(self.parents[i])
        return self.parents[i]

    def union(self, a, b):
        a_root = self.find(a)
        b_root = self.find(b)

        if a_root != b_root:
            if self.ranks[a_root] < self.ranks[b_root]:
                self.parents[a_root] = b_root
            elif self.ranks[a_root] > self.ranks[b_root]:
                self.parents[b_root] = a_root
            else:
                self.parents[a_root] = b_root
                self.ranks[b_root] += 1


if __name__ == '__main__':
    size = 20
    uf = UnionFind2(20)

    print(uf.is_connected(0, 1))
    uf.union(0, 1)
    print(uf.is_connected(0, 1))
    uf.union(0, 15)
    print(uf.is_connected(1, 15))
    uf.union(0, 4)
    uf.union(4, 5)
    print(uf.is_connected(4, 15))
    uf.union(2, 6)
    print(uf.parents)
    print(uf.ranks)
    uf.union(2, 15)
    print(uf.parents)
    print(uf.ranks)
