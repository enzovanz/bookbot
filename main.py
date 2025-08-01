import sys
from stats import get_num_words, get_char_count, get_dict_to_dict_list, get_book_text

def report(file_path ,num_words, ordered_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in ordered_list:
        if d["char"].isalpha():
            print(f'{d["char"]}: {d["num"]}')
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    frankenstein_path = sys.argv[1]
    content = get_book_text(frankenstein_path)
    num_words = get_num_words(content)
    char_dict = get_char_count(content)
    ordered_list = get_dict_to_dict_list(char_dict)
    report(frankenstein_path, num_words, ordered_list)

if __name__ == "__main__":
    main()