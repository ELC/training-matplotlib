import context
from algorithms.Sorting import bubble_original
from algorithms.Sorting import false_bubble_from_i
from algorithms.Sorting import false_bubble_from_0
from algorithms.Sorting import cocktail_bubble
from algorithms.Sorting import cocktail_selection
from algorithms.Sorting import selection
from algorithms.Sorting import insertion
import unittest
import itertools

expected = [i for i in range(5)]
permutations = itertools.permutations(expected,5)
per = [list(i) for i in permutations]

class TestSortingAlgorithms(unittest.TestCase):
    """Testing for every sorting algorithm"""

    def test_bubble_original(self):
        for i in per:
            assert bubble_original.main(i) == expected
    
    
    def test_false_bubble_from_i(self):
        for i in per:
            assert false_bubble_from_i.main(i) == expected
    
    
    def test_false_bubble_from_0(self):
        for i in per:
            assert false_bubble_from_0.main(i) == expected
    
    
    def test_cocktailbubble(self):
        for i in per:
            assert cocktail_bubble.main(i) == expected
    
    
    def test_cocktailselection(self):
        for i in per:
            assert cocktail_selection.main(i) == expected
    
    
    def test_insertion(self):
        for i in per:
            assert insertion.main(i) == expected
    
    
    def test_selection(self):
        for i in per:
            assert selection.main(i) == expected