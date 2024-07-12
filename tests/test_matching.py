"""
Test suite for word matching.
"""

# Standard libraries.
import io
import unittest

# Third-party libraries.
# None.

# Internal libraries.
from main import match_file_contents

class TestInputFile(unittest.TestCase):
    """
    Standard unit test boilerplate.
    """

    def test_matching(self) -> None:
        """
        Test that the matching function finds and counts the correct number of words.
        """
        with io.StringIO() as f:
            f.write('''Detecting first names is tricky to do even with AI.
how do you say a street name is not a first name?''')
            f.seek(0)

            predefined_words = {'ai': 0, 'detect': 0, 'name': 0}
            matches = match_file_contents(f, predefined_words)

            self.assertEqual(1, matches.get('ai', 0))
            self.assertEqual(0, matches.get('detect', 0))
            self.assertEqual(2, matches.get('name', 0))

    def test_matching_apostrophes(self) -> None:
        """
        Test that the matching function finds and counts the correct number of words.
        """
        with io.StringIO() as f:
            f.write('''My name is Colin, and I'm detecting words with apostrophes.
This is ColiN'S application, and coLin should be detected three times.
''')
            f.seek(0)

            predefined_words = {'colin': 0}
            matches = match_file_contents(f, predefined_words)

            self.assertEqual(3, matches.get('colin', 0))
