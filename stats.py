'''
this is the file where we have our functions for parsing book data to get the specific
information we want
'''

def sort_dictionaries(char_count_dict):
    '''
    takes the character dictionary and sorts it by frequency
    '''

    list_of_dicts = []
    for entry in char_count_dict:
        if entry.isalpha():
            list_of_dicts.append({"char": entry, "num": char_count_dict[entry]})
    return sorted(list_of_dicts, key=get_num_from_dict, reverse=True)

def get_num_from_dict(d):
    return d['num']

def get_char_dict(book_as_string):
    '''
    takes the long string provided and returns a dictionary of characters and their frequency
    '''
    book_as_string = book_as_string.lower()
    chars = {}
    for char in book_as_string:
        if char in chars:
            chars[char] += 1
            continue
        chars[char] = 1
    return chars

def get_word_count(book_as_string):
    '''
    takes the long string and returns the number of words
    '''
    words = book_as_string.split()
    return len(words)
