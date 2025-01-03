# Virgilio Class - Dante's Inferno Cantos

This Python script defines the `Virgilio` class to manage and work with Dante's Inferno Cantos. It includes various methods to read, analyze, and manipulate the text of the 34 Cantos, providing functionality to count verses, find specific words, and process the data in various ways.

## Introduction

This script allows you to work with the 34 Cantos of Dante's *Inferno*. You can analyze them, count specific words, find verses containing certain words, and even calculate statistics like the number of verses, tercets, and the longest verse in each Canto.

## Class Overview

### Virgilio Class

The `Virgilio` class provides methods to interact with Dante's *Inferno* text. You initialize it with a directory containing the 34 text files representing each Canto. Each Canto is expected to be stored as a `.txt` file in the provided directory, named `Canto_1.txt`, `Canto_2.txt`, ..., `Canto_34.txt`.

#### Initialization

```python
class Virgilio:
    def __init__(self, directory: str) -> None:
        """Initialize the Virgilio class with a specified directory.

```

## Methods

### read_canto_lines

Reads and returns the lines of a specific Canto.

### count_verses(self, canto_number: int)

Returns the number of verses in the specified Canto.

### count_word(self, canto_number: int, word: str)

Counts occurrences of a specified word in the Canto.

### get_verse_with_word(self, canto_number: int, word: str)

Returns the first verse containing the specified word.

### get_verses_with_word(self, canto_number: int, word: str)

Returns a list of all verses containing the specified word.

### get_longest_verse(self, canto_number: int)

Returns the longest verse in the specified Canto.

### get_longest_canto(self)

Returns the number and length of the longest Canto.

### count_words(self, canto_number: int, words: list)

Counts the occurrences of multiple words in the Canto and writes the results to a JSON file.

### get_hell_verses(self)

Returns a list of all verses from all 34 Cantos.

### count_hell_verses(self)

Returns the total number of verses across all 34 Cantos.

### get_hell_verse_mean_len(self)

Returns the average length of verses across all 34 Cantos.

## Error Handling
The script handles the following errors:

- TypeError: Raised if the canto_number is not an integer.
- CantoNotFoundError: Raised if the canto_number is outside the valid range (1-34).
- Exception: Raised for general file reading issues.
