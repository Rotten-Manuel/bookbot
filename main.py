from stats import get_book_text
from stats import get_word_counts
from stats import count_characters
from stats import sort_on
from stats import make_character_list


def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text_file = get_book_text(f"{sys.argv[1]}")
    num_words = get_word_counts(text_file)
    count = count_characters(text_file)
    chara = make_character_list(count)
    print("================== bookbot =====================")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------------- Word Count -------------------")
    print(f"{num_words}")
    print("--------------- Character Count ----------------")
    for letter in chara:
        char_letter = letter["char"]
        num_letter = letter["num"]
        print(f"{char_letter}: {num_letter}") 
    print("==================== END =======================")


main()
