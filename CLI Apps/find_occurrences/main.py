__author__ = "André Ramos"
__email__ = "fc53299@alunos.fc.ul.pt"


import sys


def read_words(file):
    """
    Reads the lines of a given file

    Args:
        file (str): Name of the file to read

    Returns:
        set(str): Set of words in the file
    """
    words = set()
    with open(file, 'r', encoding='utf8') as f:
        lines = f.read().splitlines()
     
        for line in lines:

            words_line = line.split()
            for word in words_line:
                if word not in words:
                    words.add(word)
        return words


def find_occurrences(search_file, words_set):
    """
    Count the occurrences of words and identify the lines where the words in the word_set are present.

    Args:
        search_file (str): The name of the file to be searched.
        words_set (set): A set of words to be counted.

    Returns:
        dict: A dictionary where each key represents a word from the word_set, and its corresponding value is a tuple with the count of occurrences of that word and the lines where it appears.
    """
    results = {}
    search_words = read_words(words_set)

    for word in search_words:
        with open(search_file, 'r', encoding='utf8') as f:
            count = 0
            line_count = 1
            lines = set()
            for line in f:
                list_words = line.split()
                for w in list_words:
                    found = False
                    if not found:
                        if w == word:
                            count += 1
                            lines.add(line_count)
                            found = True
                line_count += 1
        results[word] = (count, lines)
    return results


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python find_occurrences.py <search_file> <words_file>")
        sys.exit(1)

    search_file = sys.argv[1]
    words_file = sys.argv[2]

 
    occurrences = find_occurrences(search_file, words_file)
    print(occurrences)