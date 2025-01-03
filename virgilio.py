"""The script is used to create Virgilio class and work on its objects.

Author: Pamela Gacioppo
Date: 03/01/2024
"""

import json
import os


class Virgilio:
    """Class representing the management of Dante's Cantos.

    This class allows reading the lines of a specific canto (from 1 to 34) and
    provides functionality to work with the files containing the Cantos.
    """

    def __init__(self, directory: str) -> None:
        """Initialize the Virgilio class with a specified directory.

        Args:
            directory (str) -- The absolute path of the folder containing the
            34 Cantos of Dante's Inferno.
            The attribute can be set during object creation.
        """
        self.directory = directory

    class CantoNotFoundError(Exception):
        """Class handling the errors related to wrong Canto numbers."""

        def __init__(self) -> None:
            """Initialize the CantoNotFoundError with a default message."""
            super().__init__("canto_number must be between 1 and 34.")

    def read_canto_lines(self, canto_number: int, num_lines: int = None,
                         strip_lines: bool = False) -> list:
        """Read one of the Cantos specified with its number.

        It then returns a list containining the lines of the specified canto.
        The strings may be stripped and limited based on the args.

        Args:
            canto_number (int): The number of the canto to read, from 1 to 34.
            num_lines (int, optional): If provided, specifies the number of
            lines to read.
            strip_lines (bool, optional): If True, leading and trailing
            whitespace will be stripped from each line. Defaults to False.

        Raises:
            TypeError: If canto_number is not an integer.
            CantoNotFoundError: If canto_number is not between 1 and 34.
            Exception: In case of any other errors.
        """
        if not isinstance(canto_number, int):
            raise TypeError("canto_number must be an integer.")
        elif canto_number < 1 or canto_number > 34:
            raise self.CantoNotFoundError()

        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                if strip_lines:
                    if not num_lines:
                        return [line.strip() for line in file.readlines()]

                    else:
                        return [file.readline().strip()
                                for number in range(num_lines)]

                else:
                    if not num_lines:
                        return file.readlines()

                    else:
                        return [file.readline() for
                                number in range(num_lines)]

        except Exception as e:
            raise Exception(f"Error while opening {file_path}: {e}")

    def count_verses(self, canto_number: int) -> int:
        """Count the number of verses in the specified Canto.

        Args:
            canto_number (int) -- The number of the canto to read, 1 to 34.
        """
        return len(self.read_canto_lines(canto_number))

    def count_tercets(self, canto_number: int) -> int:
        """Count the number of tercets in the Canto, approximated down.

        Args:
            canto_number (int) -- The number of the canto to read, 1 to 34.
        """
        return self.count_verses(canto_number)//3

    def count_word(self, canto_number: int, word: str) -> int:
        """Count the occurrences of a specified word in the specified Canto.

        Args:
            canto_number (int) -- The number of the canto to read, 1 to 34.
            word (str) -- The word to search for in the canto.
        """
        canto_string = "\n".join(self.read_canto_lines(canto_number))

        return canto_string.count(word)

    def get_verse_with_word(self, canto_number: int, word: str) -> str:
        """Return the first verse containing the specified word.

        Args:
            canto_number (int) -- The number of the canto to read, 1 to 34.
            word (str) -- The word to search for in the canto.
        """
        for line in self.read_canto_lines(canto_number):
            if word in line:
                return (line).strip()

        return "We couldn't find the word in the text."

    def get_verses_with_word(self, canto_number: int, word: str) -> list:
        """Return a list of all the verses containing the specified word.

        Args:
            canto_number (int) -- The number of the canto to read, 1 to 34.
            word (str) -- The word to search for in the canto.
        """
        lines_with_word = [line for line in self.read_canto_lines(canto_number)
                           if word in line]

        if not lines_with_word:
            return "We couldn't find the word in the text."

        else:
            return lines_with_word

    def get_longest_verse(self, canto_number: int) -> str:
        """Return the longest verse in the specified Canto.

        Args:
            canto_number (int) -- The number of the canto to read, 1 to 34.
        """
        longest_verse = ""
        for line in self.read_canto_lines(canto_number):
            if len(line) > len(longest_verse):
                longest_verse = line
        return longest_verse.strip()

    def get_longest_canto(self) -> dict:
        """Return the number and length of the longest Canto in the folder."""
        canto_length = None
        canto_number = None
        for number in range(1, 35):
            current_canto_length = self.count_verses(number)
            if canto_length is None or current_canto_length > canto_length:
                canto_length = current_canto_length
                canto_number = number

        return {"canto_number": canto_number,
                "canto_len": canto_length,
                }

    def count_words(self, canto_number: int, words: list) -> dict:
        """Count the occurrences of words in the list within the Canto.

        It then writes the word and number of repetitions in a json file.

        Args:
            canto_number (int) -- The number of the canto to read, 1 to 34.
            words (list) -- The list of words to search for in the canto.
        """
        word_repetitions = {}
        for current_word in words:
            canto_string = "\n".join(self.read_canto_lines(canto_number))
            if current_word in canto_string:
                word = current_word
                number_of_repetitions = canto_string.count(word)
                word_repetitions[word] = number_of_repetitions

        json_file_path = os.path.join(self.directory, "word_counts.json")

        with open(json_file_path, "w", encoding="utf-8") as file:
            json.dump(word_repetitions, file, ensure_ascii=False, indent=4)

        return word_repetitions

    def get_hell_verses(self) -> list:
        """Return a list of the verses of all Cantos, from start to finish."""
        all_verses = []

        for number in range(1, 35):
            all_verses.append([line for line in self.read_canto_lines(number)])

        return all_verses

    def count_hell_verses(self) -> int:
        """Count the verses of all 34 Cantos, from start to finish."""
        total_hell_verses = 0

        for number in range(1,35):
            total_hell_verses += self.count_verses(number)

        return total_hell_verses

    def get_hell_verse_mean_len(self) -> float:
        """Return the mean length of the verses of all Cantos."""
        total_verses_length = 0.

        for number in range(1, 35):
            for line in self.read_canto_lines(number):
                total_verses_length += len(line.strip())

        return total_verses_length / self.count_hell_verses()

canti = Virgilio(
    r"C:\Users\pam19\Desktop\Epicode\Programming Principles\PP020125\canti")
