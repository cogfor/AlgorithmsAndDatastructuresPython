# -*- coding: utf-8 -*-

"""
App:
"""

from BalancedTree import BalancedTree

tree = BalancedTree()

#tree.insert(4)
#tree.insert(6)
#tree.insert(5)  # expect right/left rotation

tree.insert(4)
tree.insert(2)
tree.insert(3)  # expect left/right rotation

tree.traverseInOrder()





