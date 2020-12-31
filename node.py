class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        child_node = Node(name)
        self.children.append(child_node)
        return child_node

    def depthFirstSearch(self):
        return []

