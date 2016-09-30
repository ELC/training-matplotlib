from unittest import TestCase

from Scripts import myquicksort as my
from Tests.setup import per, a


class TestGnome(TestCase):
    def test_gnome(self):
        for i in per():
            self.assertEqual(my.gnome(list(i)), a)
