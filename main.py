import os
import sys
from pathlib import Path

from stats import get_num_words
from stats import count_characters
from stats import sort_dict
from stats import printAll


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_words_in_text(text):
    words=text.split()

    return words









    
def main():
    # Argument check
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get the book path from the command line
    book_path = Path(sys.argv[1])

    if not book_path.exists():
        print(f"Error: file '{book_path}' not found.")
        sys.exit(1)

    # Read text
    text = get_book_text(book_path)

    # Word count
    num_words = get_num_words(text)
    

    # Character count
    char_counts = count_characters(text)
    ordered=sort_dict(char_counts)
    printAll(ordered,num_words,book_path)

if __name__ == "__main__":
    main()