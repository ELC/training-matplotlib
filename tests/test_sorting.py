import context
import algorithms.Sorting as sort
import unittest
import itertools

expected = [i for i in range(5)]
permutations = itertools.permutations(expected,5)
per = [list(i) for i in permutations]

class TestSortingAlgorithms(unittest.TestCase):
    """Testing for every sorting algorithm"""

    def test_bubble_original(self):
        for i in per:
            assert sort.bubble_original.main(i) == expected
    
    
    def test_false_bubble_from_i(self):
        for i in per:
            assert sort.false_bubble_from_i.main(i) == expected
    
    
    def test_false_bubble_from_0(self):
        for i in per:
            assert sort.false_bubble_from_0.main(i) == expected
    
    
    def test_cocktailbubble(self):
        for i in per:
            assert sort.cocktail_bubble.main(i) == expected
    
    
    def test_cocktailselection(self):
        for i in per:
            assert sort.cocktail_selection.main(i) == expected
    
    
    def test_insertion(self):
        for i in per:
            assert sort.insertion.main(i) == expected
    
    
    def test_selection(self):
        for i in per:
            assert sort.selection.main(i) == expected