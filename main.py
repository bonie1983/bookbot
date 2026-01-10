from stats import counting_words # Importing the counting_words function from stats module
from stats import each_character_count # Importing the each_character_count function from stats module
from stats import final_print # Importing the final_print function from stats module

def get_book_text(path_to_file): # Function to read the content of a book from a text file
    with open(path_to_file) as f:
        return f.read()
    
def main():
    book_text = get_book_text("books/Frankenstein.txt")
    print(book_text[:1000])  # Print the first 1000 characters of the book
    counting_words(book_text) # Count and print the number of words in the book
    each_character_count(book_text) # Count and return the frequency of each character in the book
    print(each_character_count(book_text))  # Print the character frequency dictionary
    final_print(book_text) # Print the final analysis of the book
    
main()
