import unittest

from my_utils.roots import roots


class RootsTest(unittest.TestCase):
    def test_same_root(self):
        self.assertEqual(roots(1, -4, 4), (2.0, 2.0))

    def test_different_roots(self):
        self.assertEqual(roots(1, -3, 2), (1.0, 2.0))

    def test_negative_a(self):
        self.assertRaises(ValueError, roots, 0, -3, 2)

    def test_negative_discriminant(self):
        self.assertRaises(ValueError, roots, 1, 1, 1)
