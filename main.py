import sys
from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return(contents)

def main():
    # path = "books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        text = get_book_text(path)
        wordcount = count_words(text)
        letter_count = sort_letters(count_letters(text))
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {wordcount} total words")
        print("--------- Character Count -------")
        for i in letter_count:
            print(i["letter"] + ": " + str(i["num"]))

if __name__ == "__main__":
    main()
