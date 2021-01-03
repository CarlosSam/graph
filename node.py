import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

breadthFirstQueue = []

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        child_node = Node(name)
        self.children.append(child_node)
        return child_node

    def depthFirstSearch(self):
        return self.depthFirstSearchIterating([])

    def depthFirstSearchIterating(self, array):
        logger.debug('array: %s', array)
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearchIterating(array)
        return array

    def breadthFirstSearchIterate(self, result):
        result.append(self.name)
        for child in self.children:
            breadthFirstQueue.append(child)
        if (len(breadthFirstQueue) == 0):
            return result
        return breadthFirstQueue.pop(0).breadthFirstSearchIterate(result)

    def breadthFirstSearch(self):
        return self.breadthFirstSearchIterate([])

