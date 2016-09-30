from unittest import TestCase

from Scripts import myquicksort as my
from Tests.setup import per, a


class TestMyquicksortinternet(TestCase):
    def test_myquicksortinternet(self):
        for i in per():
            self.assertEqual(my.myquicksortinternet(list(i)), a)
