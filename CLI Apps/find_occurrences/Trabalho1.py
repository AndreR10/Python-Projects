__author__ = "André Ramos, 53299"
__copyright__ = "Programação II, LTI, DI/FC/UL, 2021"
__email__ = "fc53299@alunos.fc.ul.pt"


def ler_palavras(file):
    """Lê as linhas num dado ficheiro

    Args:
        file (str): Nome do ficheiro a ser lido

    Returns:
        set(str): Conjunto de palavras presentes no ficheiro
    """
    words = set()
    with open(file, 'r', encoding='utf8') as f:
        lines = f.read().splitlines()
        print(lines)
        for line in lines:
            print(line)
            words_line = line.split()
            for word in words_line:
                if word not in words:
                    words.add(word)
        return words


def encontrar_ocorrencias(search_file, words_set):
    """Contagem das palavras e 
    linhas onde se encontram presentes essas palavras

    Args:
        search_file (str): Nome do ficheiro a ser lido
        words_set (set()): Conjunto de palavras a serem encontradas

    Returns:
        dict: Devolve diciononário em que a key é a palavra
        e valor é um tuplo com o numero de vezes que essa palavra aparece e as linhas 
        onde aparece
    """
    results = {}
    search_words = ler_palavras(words_set)

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


print(encontrar_ocorrencias('turing.txt', 'palavras.txt'))