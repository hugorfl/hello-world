"""
Test cases:

1 - [TTP] Insert existing filename and one or more keywords
2 - [TTF] Insert non-existing filename and one or more keywords
3 - [TTF] No keywords provided
"""

from findWords import f_find_words
import unittest


class FindWordsTest(unittest.TestCase):
    def test_find_word_ocurrences_in_existing_file(self):
        keywords = f_find_words("lorem-ipsum.txt", "lorem", "Lorem", "et")

        self.assertDictEqual(
            d1=keywords,
            d2={'lorem': 3, 'Lorem': 2, 'et': 5}
        )

    def test_should_throw_exception_when_file_does_not_exists(self):
        with self.assertRaises(ValueError):
            f_find_words("non-existing-file", "car", "bike", "cloud")

    def test_should_throw_exception_when_no_keywords_are_provided(self):
        with self.assertRaises(ValueError):
            f_find_words("lorem-ipsum.txt")

    def test_should_throw_exception_when_filename_has_invalid_name(self):
        with self.assertRaises(ValueError):
            f_find_words("l&ore#m-ips$um.tx#t", "lorem")

    def test_should_throw_exception_when_filename_is_empty(self):
        with self.assertRaises(ValueError):
            f_find_words("", "lorem")


if __name__ == "__main__":
    unittest.main()
