class LinkedList:

    class Node:
        def __init__(self, key, value=None, next_node=None):
            self.key = key
            self.value = value
            self.next = next_node

        def __repr__(self):
            return '({}: {})'.format(self.key, self.value)

    def __init__(self):
        self.dummy_head = self.Node(None)
        self.tail
