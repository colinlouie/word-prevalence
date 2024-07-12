"""
Test suite for loading predefined words.
"""

# Standard libraries.
import io
import unittest

# Third-party libraries.
# None.

# Internal libraries.
from main import import_predefined_words

class TestPredefinedWords(unittest.TestCase):
    """
    Standard unit test boilerplate.
    """

    def test_predefined_words_loaded_correctly(self) -> None:
        """
        Test that the predefined words are loaded correctly.
        """

        with io.StringIO() as f:
            f.write('''Name
Detect
AI''')
            f.seek(0)

            predefined_words, _ = import_predefined_words(f)

            # There should be exactly three words.
            self.assertEqual(3, len(predefined_words))

            # These should be the three words in canonical form.
            self.assertTrue('ai' in predefined_words)
            self.assertTrue('detect' in predefined_words)
            self.assertTrue('name' in predefined_words)
