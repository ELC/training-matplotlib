from sumado import mainfunction
import unittest


class TestMainFunction(unittest.TestCase):

    def test_get_pairs(self):
        input_ = [1, 2, 3, 4]
        output = {
            1: [2, 3, 4],
            2: [3, 4],
            3: [4]
            }
        result = mainfunction.get_pairs(input_)
        self.assertEqual(result, output)

    def test_clean_vertex(self):
        adj = {
            1: [2, 3, 4],
            2: [1, 3, 4],
            3: [1, 2, 4],
            4: [1, 2, 3]
            }
        vertex = 4
        output = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2],
            4: [1, 2, 3]
            }
        mainfunction.clean_vertex(adj, vertex)
        self.assertEqual(adj, output)
