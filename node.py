import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

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
        queue = [self]
        while (len(queue) > 0):
            node = queue.pop(0)
            result.append(node.name)
            for child in node.children:
                queue.append(child)
        return result

    def breadthFirstSearch(self):
        return self.breadthFirstSearchIterate([])

