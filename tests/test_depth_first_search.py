import unittest
from node import Node

class TestDepthFirstSearch(unittest.TestCase):

    def test_trivial_case(self):
        simple_graph = Node('simple')
        self.assertEqual(simple_graph.depthFirstSearch(), [])

if __name__ == '__main__':
    unittest.main()

