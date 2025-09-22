def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def get_word_counts(book):
    word_list = book.split()
    num_words = len(word_list)
    return f"Found {num_words} total words"

def count_characters(text):
    book = text.lower()
    letters_dic = {}
    for letter in book:
        if letter not in letters_dic:
            letters_dic[letter] = 1
        else:
            letters_dic[letter] += 1
    return letters_dic

def sort_on(dic):
    return dic["num"]

def make_character_list(dic):
    letter_list = []
    for letter in dic:
        dictionary = {}
        dictionary["char"] = letter
        dictionary["num"] = dic[letter]
        letter_list.append(dictionary)
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list


