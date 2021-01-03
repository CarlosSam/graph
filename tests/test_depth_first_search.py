import unittest
from node import Node
from tests.graph_info import simple_graph_info, graph1_info, graph2_info, graph3_info, graph4_info, graph5_info

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
        self.assertEqual(trivial_graph.depthFirstSearch(), ['trivial'])

    def test_simple_graph(self):
        simple_graph = loadGraph(simple_graph_info)
        self.assertEqual(simple_graph.depthFirstSearch(), ['A', 'B', 'C'])

    def test_graph1(self):
        graph1 = loadGraph(graph1_info)
        self.assertEqual(graph1.depthFirstSearch(), ['A', 'B', 'E', 'F', 'I', 'J', 'C', 'D', 'G', 'K', 'H'])

    def test_graph2(self):
        graph2 = loadGraph(graph2_info)
        self.assertEqual(graph2.depthFirstSearch(), ['A','B','D','C'])

    def test_graph3(self):
        graph3 = loadGraph(graph3_info)
        self.assertEqual(graph3.depthFirstSearch(), ['A','B','C','F','D','E'])

    def test_graph4(self):
        graph4 = loadGraph(graph4_info)
        self.assertEqual(graph4.depthFirstSearch(), ['A', 'B', 'C', 'D','F','E'])

    def test_graph5(self):
        graph5 = loadGraph(graph5_info)
        self.assertEqual(graph5.depthFirstSearch(), ['A',"B","G","H","O","P","T","U","Q","R",'V',"W","X",'Z',"Y","I","C",'J',"D", "K",'S',"L", "E", "F", "M","N"])


if __name__ == '__main__':
    unittest.main()

