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

    def breadthFirstSearchIterate(self, roots, result):
        logger.debug('roots: %s, result: %s', [node.name for node in roots], [n for n in result])
        if len(roots) == 0:
            return result
        new_roots = []
        for node in roots:
            result.append(node.name)
            for child in node.children:
                new_roots.append(child)
        return self.breadthFirstSearchIterate(new_roots, result)

    def breadthFirstSearch(self):
        return self.breadthFirstSearchIterate([self], [])

