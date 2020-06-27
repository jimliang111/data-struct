import time
from bstset import BSTSet
from trie import Trie
import fileoperator


if __name__ == '__main__':
    t = Trie()
    bst_set = BSTSet()

    filename = 'pride-and-prejudice.txt'
    total = list(fileoperator.load(filename))

    print(filename)
    print('Total words:', len(total))

    start = time.time()
    for word in total:
        bst_set.add(word)

    for word in total:
        bst_set.contains(word)
    cost = time.time() - start

    print('Total different words:', bst_set.size())
    print('BST Set: {:.6f}s'.format(cost))

    print()

    start = time.time()
    for word in total:
        t.add(word)

    for word in total:
        t.contains(word)
    cost = time.time() - start

    print('Total different words:', t.size())
    print('Trie: {:.6f}s'.format(cost))
