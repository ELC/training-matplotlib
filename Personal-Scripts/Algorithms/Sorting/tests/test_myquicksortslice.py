from unittest import TestCase

from Scripts import myquicksort as my
from Tests.setup import per, a


class TestMyquicksortslice(TestCase):
    def test_myquicksortslice(self):
        for i in per():
            self.assertEqual(my.myquicksortslice(list(i)), a)
