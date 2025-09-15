def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    text_file = get_book_text("./books/frankenstein.txt")
    text_words = text_file.split()
    num_words = len(text_words)
    print(f"{num_words} words found in the document")

main()
