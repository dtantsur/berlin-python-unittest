import unittest
from unittest import mock

from my_utils import roots


class RootsTest(unittest.TestCase):
    def test_correct(self):
        self.assertEqual(roots.roots(1, -3, 2),
                         (1.0, 2.0))

    def test_negative_a(self):
        self.assertRaisesRegex(ValueError, 'a cannot be zero',
                               roots.roots, 0, -3, 2)

    def test_negative_discriminant(self):
        self.assertRaisesRegex(ValueError, 'discriminant below zero',
                               roots.roots, 1, 1, 1)


@mock.patch('builtins.print', autospec=True)
class MainTest(unittest.TestCase):

    @mock.patch('sys.argv', [None, '1', '-3', '2'])
    def test_correct(self, mock_print):
        roots.main()
        mock_print.assert_called_once_with((1.0, 2.0))

    @mock.patch('sys.exit', autospec=True)
    @mock.patch('sys.argv', [None, '1', '-3'])
    def test_missing_argument(self, mock_exit, mock_print):
        mock_exit.side_effect = RuntimeError
        self.assertRaises(RuntimeError, roots.main)
        mock_exit.assert_called_once_with('3 arguments required')
        mock_print.assert_not_called()
