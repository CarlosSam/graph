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
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearchIterating(array)
        return array

