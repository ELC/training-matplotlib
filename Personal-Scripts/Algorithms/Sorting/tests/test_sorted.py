from unittest import TestCase
from Tests import setup


class TestSorted(TestCase):
    def test_sorted(self):
        for i in setup.per():
            self.assertEqual(sorted(list(i)), setup.a)
