import unittest
from node import Node
from tests.utils import loadGraph
from tests.graph_info import simple_graph_info, graph1_info, graph2_info, graph3_info, graph4_info, graph5_info

class TestBreadthFirstSearch(unittest.TestCase):

    def test_trivial_case(self):
        trivial_graph = Node('trivial')
        self.assertEqual(trivial_graph.breadthFirstSearch(), ['trivial'])

    def test_simple_graph(self):
        simple_graph = loadGraph(simple_graph_info)
        self.assertEqual(simple_graph.breadthFirstSearch(), ['A', 'B', 'C'])

    def test_graph1(self):
        graph1 = loadGraph(graph1_info)
        self.assertEqual(graph1.breadthFirstSearch(), ['A', "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"])

    def test_graph5(self):
        graph5 = loadGraph(graph5_info)
        self.assertEqual(graph5.breadthFirstSearch(), ['A', "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])


if __name__ == '__main__':
    unittest.main()

