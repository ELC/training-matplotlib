import context
import algorithms.Sorting as sort
import unittest
import itertools

expected = [i for i in range(5)]
permutations = itertools.permutations(expected,5)
per = [list(i) for i in permutations]

class TestMainFunction(unittest.TestCase):
    """Testing for every sorting algorithm"""

    def test_bubble_original():
        for i in per:
            assert sort.bubble_original.main(i) == expected
    
    
    def test_false_bubble_from_i():
        for i in per:
            assert sort.false_bubble_from_i.main(i) == expected
    
    
    def test_false_bubble_from_0():
        for i in per:
            assert sort.false_bubble_from_0.main(i) == expected
    
    
    def test_cocktailbubble():
        for i in per:
            assert sort.cocktail_bubble.main(i) == expected
    
    
    def test_cocktailselection():
        for i in per:
            assert sort.cocktail_selection.main(i) == expected
    
    
    def test_insertion():
        for i in per:
            assert sort.insertion.main(i) == expected
    
    
    def test_selection():
        for i in per:
            assert sort.selection.main(i) == expected