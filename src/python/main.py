"""
Given a list of predefined words and a file to match against, this script will output the count of each predefined word.
"""

# Standard libraries.
import re
from collections import OrderedDict, defaultdict
from typing import Dict, IO, Tuple

# Third-party libraries.
# None.

# Internal libraries.
# None.

def import_predefined_words(predefined_words_f: IO[str]) -> Tuple[Dict[str, int], Dict[str, str]]:
    """
    Given a file handle, parses a list of predefined words to match against, where each word is on a new line.

    Assumptions: words are case-insensitive, and does not contain any punctuation.

    Output will be a tuple of two dictionaries:
        1. A dictionary of predefined words in a canonical form.
        2. A dictionary mapping the canonical form to the original case.

    Input (file) example:
        Name\n
        Detect\n
        AI\n

    Output example:
        (
            {
                'name': 0,
                'detect': 0,
                'ai': 0
            },
            {
                'name': 'Name',
                'detect': 'Detect',
                'ai': 'AI'
            }
        )
    """

    # Store the predefined words in a canonical form.
    predefined = {}

    # Map the canonical form to the original case.
    predefined_map = {}

    for line in predefined_words_f:
        for word in line.strip().split():
            predefined[word.lower()] = 0
            predefined_map[word.lower()] = word
    return predefined, predefined_map

def match_file_contents(match_f: IO[str], predefined_words: Dict[str, int]) -> Dict[str, int]:
    """
    Give a file handle and a dictionary of predefined words, returns a dictionary of matches against predefined words,
    and their respective counts.

    Output example:
        {
            'ai': 0,
            'detect': 1,
            'name': 2
        }
    """
    matches = defaultdict(int)

    # Read the file line by line, word by word, ignoring punctuation, then lowercase.
    for line in match_f:
        for word in re.findall(r'\b\w+\b', line):
            candidate = word.lower()
            if candidate in predefined_words:
                matches[candidate] += 1
    return matches

def output_matches(matches: Dict[str, int], predefined_map: Dict[str, str]) -> None:
    """
    Given a dictionary of matches and their counts, will output
    """
    column_titles = ['Predefined word', 'Match count']
    longest_word_len = len(column_titles[0])
    for word in matches.keys():
        longest_word_len = max(longest_word_len, len(word))

    # Sort the matches by descending count.
    descending_prevalence = OrderedDict(sorted(matches.items(), key=lambda t: t[1], reverse=True))

    print(f'{column_titles[0]:<{longest_word_len}}   {column_titles[1]}')
    for word, count in descending_prevalence.items():
        print(f'{predefined_map[word]:<{longest_word_len}}   {count}')

def main():
    """
    Application entry point.
    """
    with open('predefined-words.txt', 'r', encoding='utf-8') as predfined_words_file:
        predefined_words, predefined_map = import_predefined_words(predfined_words_file)
    with open('input.txt', 'r', encoding='utf-8') as input_file:
        matches = match_file_contents(input_file, predefined_words)
    output_matches(matches, predefined_map)

if __name__ == '__main__':
    main()
