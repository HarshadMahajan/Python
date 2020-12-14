import unittest
from unorderedlist import UnorderedList

class TestUnorderedList(unittest.TestCase):
    def setUp(self):
        self.data = UnorderedList()
        self.data.add(1)
        self.data.add(2)
        self.data.add(3)

    def test_one_plus_one_equals_two(self):
        self.assertEqual(2, 1+1)
