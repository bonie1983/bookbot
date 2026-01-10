from stats import get_book_text # Importing the get_book_text function from stats module
from stats import counting_words # Importing the counting_words function from stats module
from stats import each_character_count # Importing the each_character_count function from stats module
from stats import final_print # Importing the final_print function from stats module
import sys
    
def main():
    final_print(book_text) # Print the final analysis of the book


# Entry point of the script    
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_text = get_book_text(sys.argv[1])
main()