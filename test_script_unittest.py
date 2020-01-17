import unittest
import script

class TestScript(unittest.TestCase):
    
    def test_parse_csv(self):
        result = script.parse_csv('test_parse_method.csv')
        self.assertEqual(result, [('a', 'b', 7), ('a', 'c', 9)])

    def test_shortest_path(self):
        graph = script.Graph([("a", "b", 7), ("a", "c", 9), ("a", "f", 14), ("b", "c", 10),
                              ("b", "d", 15), ("c", "d", 11), ("c", "f", 2), ("d", "e", 6),
                              ("e", "f", 9), ("m", "n", 12)])
        self.assertEqual(graph.dijkstra("a", "e"), "Result: 4 stops, 26 minutes")
        self.assertEqual(graph.dijkstra("a", "m"), "No routes from a to m")
        self.assertEqual(graph.dijkstra("a", "y"), "Please provide valid stations")

    def test_main(self):
        edges = script.parse_csv('test_route.csv')
        graph = script.Graph(edges)
        self.assertEqual(graph.dijkstra("a", "e"), "Result: 4 stops, 26 minutes")

if __name__ == '__main__':
    unittest.main()
