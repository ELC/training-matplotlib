import unittest
import context
import sumado.mainfunction as main
import json


class TestMainFunction(unittest.TestCase):

    def test_get_pairs(self):
        input_ = [1, 2, 3, 4]
        output = {
            1: [2, 3, 4],
            2: [3, 4],
            3: [4]
            }
        result = main.get_pairs(input_)
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
        main.clean_vertex(adj, vertex)
        self.assertEqual(adj, output)


class TestDefaultCases(unittest.TestCase):
    def test_triangle(self):
        input_ = [1, 2, 3, 4, 5, 6]
        expected = {
                    "vertexes": [1, 2, 3, 4, 5, 6],
                    "poligons": [7, 10, 11, 15]
                   }
        output_raw = main.main("tri_v1", input_)
        output = json.loads(output_raw)
        self.assertEqual(output, expected)

    def test_2x3_v1(self):
        input_ = [1, 2, 3, 4, 5, 6]
        expected = {
                    "vertexes": [1, 2, 3, 4, 5, 6],
                    "poligons": [8, 10, 16]
                   }
        output_raw = main.main("2x3_v1", input_)
        output = json.loads(output_raw)
        self.assertEqual(output, expected)

    def test_3x3_v1(self):
        input_ = [8, 5, 9, 1, 7, 6, 2, 3, 4]
        expected = {
                    "vertexes": [8, 5, 9, 1, 7, 6, 2, 3, 4],
                    "poligons": [20, 16, 27, 13, 17, 14]
                   }
        output_raw = main.main("3x3_v1", input_)
        output = json.loads(output_raw)
        self.assertEqual(output, expected)

    def test_4x4_v1(self):
        input_ = [7, 2, 6, 10, 8, 13, 1, 12, 15, 11, 3, 16, 5, 9, 4, 14]
        expected = {
                    "vertexes": [7, 2, 6, 10, 8, 13, 1, 12, 15, 11, 3, 16, 5,
                                 9, 4, 14],
                    "poligons": [17, 22, 23, 28, 19, 47, 28, 32, 35, 29, 27,
                                 23, 34]
                   }
        output_raw = main.main("4x4_v1", input_)
        output = json.loads(output_raw)
        self.assertEqual(output, expected)
