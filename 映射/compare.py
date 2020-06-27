import time

from avltree import AVLTree
from bst2 import BST2
from rbtree2 import RBTree2
from hashtable import HashTable
import fileoperator

if __name__ == '__main__':
    filename = 'pride-and-prejudice.txt'
    total = list(fileoperator.load(filename))
    bst_map = BST2()

    print(filename)
    print('Total words:', len(total))

    start = time.time()
    for word in total:
        if word not in bst_map:
            bst_map[word] = 1
        else:
            bst_map[word] += 1

    for word in total:
        word in bst_map
    end = time.time() - start

    print('Total different words:', len(bst_map))
    print('Frequency of pride:', bst_map['pride'])
    print('Frequency of prejudice:', bst_map['prejudice'])
    print('bst-tree map: {:.6f}'.format(end))

    avl_map = AVLTree()

    print()
    print('Total words:', len(total))

    start = time.time()
    for word in total:
        if word not in avl_map:
            avl_map[word] = 1
        else:
            avl_map[word] += 1

    for word in total:
        avl_map.contains(word)
    end = time.time() - start

    print('Total different words:', len(avl_map))
    print('Frequency of pride:', avl_map['pride'])
    print('Frequency of prejudice:', avl_map['prejudice'])
    print('avl-tree map: {:.6f}'.format(end))

    rb_tree = RBTree2()

    print()
    print('Total words:', len(total))

    start = time.time()
    for word in total:
        if word not in rb_tree:
            rb_tree[word] = 1
        else:
            rb_tree[word] += 1

    for word in total:
        word in rb_tree
    end = time.time() - start

    print('Total different words:', len(rb_tree))
    print('Frequency of pride:', rb_tree['pride'])
    print('Frequency of prejudice:', rb_tree['prejudice'])
    print('rb-tree map: {:.6f}'.format(end))

    base_dict = {}

    print()
    print('Total words:', len(total))

    start = time.time()
    for word in total:
        base_dict[word] = base_dict.get(word, 0) + 1

    for word in total:
        word in base_dict
    end = time.time() - start

    print('Total different words:', len(base_dict))
    print('Frequency of pride:', base_dict['pride'])
    print('Frequency of prejudice:', base_dict['prejudice'])
    print('build-in dict: {:.6f}'.format(end))

    hash_table = HashTable()

    print()
    print('Total words:', len(total))

    start = time.time()
    for word in total:
        if word not in hash_table:
            hash_table[word] = 1
        else:
            hash_table[word] += 1

    for word in total:
        hash_table.contains(word)
    end = time.time() - start

    print('Total different words:', len(hash_table))
    print('Frequency of pride:', hash_table['pride'])
    print('Frequency of prejudice:', hash_table['prejudice'])
    print('hash map: {:.6f}'.format(end))
