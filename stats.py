import sys

def get_book_text(path_to_file): # Function to read the content of a book from a text file
    with open(path_to_file) as f:
        return f.read()

def counting_words(text): # Function to count the number of words in the text
    words = text.split()
    num_of_words = len(words)
    return num_of_words #print(f'Found {num_of_words} total words')

def each_character_count(text):
    char_count = {}
    for char in text:
        char = char.lower()  # Normalize to lowercase
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sorted_character_count(text):
    char_count = each_character_count(text) # Get the character count dictionary
    filtered_count = {char: count for char, count in char_count.items() if char.isalpha()} # Filter only alphabetic characters
    sorted_count = dict(sorted(filtered_count.items())) # Sort the dictionary by character
    return sorted_count

# final print function
def final_print(text):
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {sys.argv[1]}')
    print("----------- Word Count ----------")
    print(f"Found {counting_words(text)} total words")
    print("--------- Character Count -------")
    for char, count in sorted_character_count(text).items():
        print(f"{char}: {count}")
    print ("============= END ===============")