import sys
from stats import get_word_count, get_char_count, get_sorted_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    try:
        book_path = sys.argv[1]
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = (get_book_text(book_path))
    word_count = get_word_count(book_text) 
    char_count = get_char_count(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for letter in get_sorted_chars(char_count):
        if letter["char"].isalpha():
            print(f"{letter["char"]}: {letter["num"]}")

    print("============= END ===============")

main()
