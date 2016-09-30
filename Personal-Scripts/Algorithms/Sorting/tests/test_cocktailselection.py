from unittest import TestCase

from Scripts import myquicksort as my
from Tests.setup import per, a


class TestCocktailselection(TestCase):
    def test_cocktailselection(self):
        for i in per():
            self.assertEqual(my.cocktailselection(list(i)), a)
