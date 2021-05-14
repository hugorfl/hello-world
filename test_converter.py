"""
Test Cases:

1 - [TTP] Insert positive integer number
2 - [TTP] Insert 0
3 - [TTP] Insert integer number with leading zeros
4 - [TTP] Insert large numbers (Eg. 68719476736)
5 - [TTF] Insert -1
6 - [TTF] Insert floating point number
7 - [TTF] Insert alphanumeric
8 - [TTF] Insert regular characters
9 - [TTF] Insert symbols
10 - [TTF] No arguments provided

TTP: Test to pass
TTF: Test to fail
"""

from converter2X import convert_to_bin
from converter2X import convert_to_hex
import unittest


class ConversionTest(unittest.TestCase):
    def test_pass_can_convert_positive_integer_number(self):
        self.assertEqual("11100", convert_to_bin(28))
        self.assertEqual("1C", convert_to_hex(28))

    def test_pass_can_convert_zero(self):
        self.assertEqual("0", convert_to_bin(0))
        self.assertEqual("0", convert_to_hex(0))

    def test_pass_can_convert_string_with_leading_zeros(self):
        self.assertEqual("1101", convert_to_bin("0013"))
        self.assertEqual("D", convert_to_hex("0013"))

    def test_pass_can_convert_large_numbers(self):
        self.assertEqual(
            "1000000000000000000000000000000000000",
            convert_to_bin(68719476736)
        )
        self.assertEqual("1000000000", convert_to_hex(68719476736))

    def test_fail_should_not_convert_negative_numbers(self):
        with self.assertRaises(ValueError):
            convert_to_bin(-1)

        with self.assertRaises(ValueError):
            convert_to_hex(-1)

    def test_fail_should_not_convert_floating_point_numbers(self):
        with self.assertRaises(ValueError):
            convert_to_bin(5.0)

        with self.assertRaises(ValueError):
            convert_to_hex(5.0)

    def test_fail_should_not_convert_alphanum_str(self):
        with self.assertRaises(ValueError):
            convert_to_bin("1F")

        with self.assertRaises(ValueError):
            convert_to_hex("1F")

    def test_fail_should_not_convert_alpha_str(self):
        with self.assertRaises(ValueError):
            convert_to_bin("hello")

        with self.assertRaises(ValueError):
            convert_to_hex("hello")

    def test_fail_should_not_convert_special_char_str(self):
        with self.assertRaises(ValueError):
            convert_to_bin("#$%&/(")

        with self.assertRaises(ValueError):
            convert_to_hex("#$%&/(")

    def test_fail_should_not_accept_empty_str(self):
        with self.assertRaises(ValueError):
            convert_to_bin("")

        with self.assertRaises(ValueError):
            convert_to_hex("")

    def test_fail_should_not_accept_none_as_argument(self):
        with self.assertRaises(ValueError):
            convert_to_bin(None)

        with self.assertRaises(ValueError):
            convert_to_hex(None)


if __name__ == "__main__":
    unittest.main()
