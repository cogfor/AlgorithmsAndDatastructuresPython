# -*- coding: utf-8 -*-

"""
Node.py: Describes a single node
"""


class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None

    def remove(self, data, previousNode):
        if self.data == data:
            previousNode.nextNode = self.nextNode
            del self.data
            del self.nextNode
        else:
            if self.nextNode is not None:
                self.nextNode.remove(data, self)
