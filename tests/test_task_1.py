import unittest
from task_1 import reverse_check


class TestReverseCheck(unittest.TestCase):

    def test_correct_reverse_of_positive_input(self):
        expected = '123456789'
        self.assertEqual(reverse_check('987654321'), expected)

    def test_correct_reverse_of_negative_input(self):
        expected = '-56789'
        self.assertEqual(reverse_check('-98765'), expected)

    def test_return_0_if_reversed_positive_number_exceeds_32bits(self):
        expected = '0'
        self.assertEqual(reverse_check('10000000001'), expected)

    def test_return_0_if_reversed_negative_number_exceeds_32bits(self):
        expected = '0'
        self.assertEqual(reverse_check('-10000000001'), expected)
