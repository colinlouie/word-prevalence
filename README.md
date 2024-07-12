# Word prevalence

This application reads an input file and finds matches against a predefined set of words.

There can be up to 10K entries in the list of predefined words.

The output of the program should look something like this:

```
Predefined word           Match count
FirstName                 3500
LastName                  2700
Zipcode                   1601
```

# Requirements

The input file is a plain text (ASCII) file -- every record separated by a new line.

For this exercise, assume English words only.

The file size can be up to 20 MB.

The predefined words are defined in a text file, every word separated by a newline. Use a sample file of your choice for
the set of predefined keywords for the exercise.

Assume that the predefined words file doesn’t contain duplicates.

Maximum length of the word can be upto 256.

Matches should be case-insensitive.

The match should be word to word match, no substring matches.

Consider a sample file with only the following two lines:

```
Line 1: Detecting first names is tricky to do even with AI.
Line 2: how do you say a street name is not a first name?
```

And a sample list of predefined words:

```
Name
Detect
AI
```

The match should happen only for the word “AI” in the first line and the word “name” in the second line.  The word
“Detect” should not match.

If there is any aspect of the requirement or question is not clear, please make reasonable assumptions and document them
in the README file to be submitted with the assignment.

# Approach / design decisions

I would store the predefined words, canonicalized (via lowercase) in a dictionary.

I would then iterate the the input file line by line, and within a line, iterate word by word, canonicalizing each word
(stripping punctuation, lowercasing). If said word is a match against the predefined words dictionary, increment the
prevalence.

As for the output, the requirements infer that the prededefined words are not canonicalized and I will choose to keep
them in their original case. The requirements also infer that the results are sorted by descending prevalence. Both
columns appear to be left-justified.

# Considerations

There can be up to 10,000 predefined words, at a maximum of 256 characters. This occupies 2,560,000 bytes, or 2.44MB
(2,560,000 bytes / 1,024 bytes/KB / 1,024 KB/MB) of memory (excluding the language's data structure overhead). A
dictionary is appropriate for this size of data, and will provide quick O(1) access to incrementing prevalence count.

With an input file of 20MB (or 20,971,520 bytes), I plan on iterating line by line, and with the worst case of a single
line of words (no newlines in the file at all), this should fit into memory on most modern computers. If requirements
were to change significantly (in the order of magnitude which would exceed available system memory), then I would change
the approach to iterate word by word by moving a file pointer, or use a framework such as Apache Spark.

# Development environment

- macOS Sonoma 14.5
- Intel CPU
- Python 3.12.3

## Test case execution

This covers loading of the predefined words, as well as parsing of the input file. Not included in this repository is
test coverage of Lorem Ipsum repeated up to 20MB for performance testing.

This is intended to be executed from the repository root:

```shell
PYTHONPATH=src/python pytest --no-header -v
```

Example output:
```
============================================== test session starts ==============================================
collected 2 items

tests/test_matching.py::TestInputFile::test_matching PASSED                                               [ 50%]
tests/test_predefined_words.py::TestPredefinedWords::test_predefined_words_loaded_correctly PASSED        [100%]

=============================================== 2 passed in 0.02s ===============================================
```

## Application execution

This is intended to be executed from the repository root:

```shell
python3 src/python/main.py
```

Example output:
```
Predefined word   Match count
Name              2
AI                1
```

## Linting

Find all Python source files:
```shell
find . -type f -name "*.py"
```

Example output:
```
./tests/test_matching.py
./tests/test_predefined_words.py
./src/python/main.py
```

Lint all Python source files:
```shell
find . -type f -name "*.py" | xargs pylint --verbose
```

Example output:
```
Using config file $REPOROOT/.pylintrc

-----------------------------------------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
Checked 3 files, skipped 0 files
```
