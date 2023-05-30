# Project Name

Find Occurrences

## Description

This project is a simple Python script that reads a text file and searches for occurrences of specific words in it. It provides a function `find_occurrences` that counts the occurrences of words and identifies the lines where the words are present. The script takes two command-line arguments: the file to be searched and a file containing a list of words to be counted. The output is a dictionary where each key represents a word from the word set, and its corresponding value is a tuple with the count of occurrences of that word and the lines where it appears.

## Prerequisites

- Python 3.x

## Installation

Clone the repository:

```bash
git clone https://github.com/AndreR10/Python-Projects.git
```

Change to the project directory:

```bash
cd CLI\Apps/find_occurrences
```

(Optional) Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

- For Windows:

```bash
venv\Scripts\activate
```

- For macOS/Linux:

```bash
source venv/bin/activate
```

## Usage

```bash
python find_occurrences.py <search_file> <words_file>
```

- `<search_file>`: The name of the file to be searched.
- `<words_file>`: The name of the file containing the list of words to be counted.

Example:

```bash
python find_occurrences.py text.txt words.txt
```

## Function Documentation

### `read_words(file)`

Reads the lines of a given file and returns a set of words.

**Arguments:**

- `file` (str): Name of the file to read.

**Returns:**

- `set(str)`: Set of words in the file.

### `find_occurrences(search_file, words_set)`

Count the occurrences of words and identify the lines where the words in the `words_set` are present.

**Arguments:**

- `search_file` (str): The name of the file to be searched.
- `words_set` (set): A set of words to be counted.

**Returns:**

- `dict`: A dictionary where each key represents a word from the `words_set`, and its corresponding value is a tuple with the count of occurrences of that word and the lines where it appears.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

- Author: André Ramos
- Email: fc53299@alunos.fc.ul.pt
