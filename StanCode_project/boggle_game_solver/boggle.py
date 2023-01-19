"""
File: boggle.py
Name:
----------------------------------------
"""
import time
FILE = 'dictionary.txt'


def main():
    """
    input 4 rows of letters,
    and find all the words in boggle game
    """
    start = time.time()
    dic_list = read_dictionary()
    letters = []
    counts = []
    for i in range(4):
        input_letter = input(f'{i+1} row of letters: ').lower().split()
        for ch in input_letter:
            if len(ch) != 1 or len(input_letter) != 4:
                print('Illegal input')
                break
        letters.append(input_letter)
    for i in range(4):
        for j in range(4):
            position = []
            word = ''
            word += letters[i][j]
            position.append((i, j))
            find_word(letters, dic_list, counts, word, position, (i, j), (i, j))
    print(f'There are {len(counts)} words in total.')
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_word(letters, dic_list, counts, word, position, last_position, current_position):
    """
    :param letters: list of input letters
    :param dic_list: list,dictionary
    :param counts: list, count the total found words
    :param word: str, the word contains letters
    :param position: the word's position
    :param last_position: position of last letter
    :param current_position: position of current letter
    """
    last_position = current_position
    if has_prefix(word, dic_list):
        # Base case
        if word in dic_list and len(word) >= 4:
            counts.append(1)
            print(f'Found "{str(word)}"')
            dic_list.remove(word)
            find_word(letters, dic_list, counts, word, position, last_position, current_position)
        else:
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    x = last_position[0] + i
                    y = last_position[1] + j
                    if 0 <= x < 4 and 0 <= y < 4:
                        if (x, y) not in position:
                            position.append((x, y))
                            # choose
                            word += letters[x][y]
                            current_position = (x, y)
                            # explore
                            find_word(letters, dic_list, counts, word, position, last_position, current_position)
                            # un choose
                            position.pop()
                            word = word[:-1]


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    dic_list = []
    with open(FILE, 'r') as f:
        for line in f:
            dic_list += line.split()
    return dic_list


def has_prefix(sub_s, dic_list):
    """
     :param dic_list: list, dictionary
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for ch in dic_list:
        if ch.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
