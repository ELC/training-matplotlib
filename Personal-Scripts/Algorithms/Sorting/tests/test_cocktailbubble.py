from unittest import TestCase

from Scripts import myquicksort as my
from Tests.setup import per, a


class TestCocktailbubble(TestCase):
    def test_cocktailbubble(self):
        for i in per():
            self.assertEqual(my.cocktailbubble(list(i)), a)
