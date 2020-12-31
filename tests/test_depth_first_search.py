import unittest
from node import Node
from tests.graph_info import simple_graph_info

def loadGraphRecursive(node, info):
    node_info = next(filter(lambda current_node_info: current_node_info['id'] == node.name, info['nodes']))
    for child_name in node_info['children']:
        child_node = node.addChild(child_name)
        loadGraphRecursive(child_node, info)
    return node

def loadGraph(info):
    root = Node(info['startNode'])
    loadGraphRecursive(root, info)
    return root


class TestDepthFirstSearch(unittest.TestCase):

    def test_trivial_case(self):
        trivial_graph = Node('trivial')
        self.assertEqual(trivial_graph.depthFirstSearch(), [])

    def test_simple_graph(self):
        simple_graph = loadGraph(simple_graph_info)
        self.assertEqual(simple_graph.depthFirstSearch(), ['A', 'B', 'C'])


if __name__ == '__main__':
    unittest.main()

