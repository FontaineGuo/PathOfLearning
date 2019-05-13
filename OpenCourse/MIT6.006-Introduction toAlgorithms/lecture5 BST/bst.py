#!/usr/bin/python3
# -*- coding: utf-8 -*

class BSTNode(object):
    
    def __init__(self, parent, k):
        """
         Args:
            parent: The node's parent.
            k: key of the node.
        """
        self.key = k
        self.parent = parent
        self.left = None
        self.right = None

    def _str(self):
        return self.key


    def insert(self, node):
        if node is None:
            return 
        if node.key < self.key:
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.insert(node)

    def delete(self):
        pass

class BST(object):

    def __init__(self, klass = BSTNode):
        self.root = None
        self.klass = klass

    def insert(self, k):
        node = self.klass(None, k)
        if self.root is None: 
            self.root = node
        else:
            self.root.insert(node)
        return node


def test():
    items = [49, 79,46,41,64, 83]
    tree = BST()

    for item in items:
        tree.insert(item)

    print(tree.root.key)
    left_sub = tree.root.left
    right_sub = tree.root.right

    print(left_sub.key)
    print(right_sub.key)

    print(left_sub.left.key)
    print(right_sub.left.key)
    print(right_sub.right.key)


if __name__ == '__main__': test()