'''
book bot from boot.dev tutorial
'''

import sys
import stats

def main():
    '''
    entry point for our code
    '''
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_location = sys.argv[1]

    word_count = stats.get_word_count(get_book_text(book_location))
    char_dict = stats.get_char_dict(get_book_text(book_location))
    sorted_list_of_dicts = stats.sort_dictionaries(char_dict)

    print_report(word_count, sorted_list_of_dicts, book_location)


def get_book_text(path):
    '''
    gets the entire contents of a text file and returns it
    '''
    with open(path, "r", encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents


def print_report(word_count, sorted_list, book_location):
    '''
    pretty print the information we've collected about the book we chose
    '''
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_list:
        print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")


main()
