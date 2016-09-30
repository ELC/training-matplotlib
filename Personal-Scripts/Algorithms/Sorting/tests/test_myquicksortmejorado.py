from unittest import TestCase

from Scripts import myquicksort as my
from Tests.setup import per, a


class TestMyquicksortmejorado(TestCase):
    def test_myquicksortmejorado(self):
        for i in per():
            self.assertEqual(my.myquicksortmejorado(list(i)), a)
