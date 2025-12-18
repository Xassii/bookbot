import sys
from stats import count_words, count_chars, sort_dict_list

def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()


def main():
    args = sys.argv
    if not len(args) == 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    
    text = get_book_text(args[1])
    print(f'Found {count_words(text)} total words')
    
    print('--------- Character Count -------')
    
    char_dict = count_chars(text)
    char_list = [{'char' : c, 'num': i} for c, i in char_dict.items()]
    sorted_list = sort_dict_list(char_list)
    
    for d in sorted_list:
        if d['char'].isalpha():
            print(f'{d['char']}: {d['num']}')
    
    print('============= END ===============')


if __name__ == '__main__':
    main()