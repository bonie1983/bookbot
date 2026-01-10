def counting_words(text): # Function to count the number of words in the text
    words = text.split()
    num_of_words = len(words)
    return print(f'Found {num_of_words} total words')

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
    char_count = each_character_count(text)
    sorted_count = dict(sorted(char_count.items()))
    return sorted_count

def final_print(text):
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {text}')
    print("----------- Word Count ----------")
    print(f"Found {counting_words(text)} total words")
    print("--------- Character Count -------")
    for char, count in sorted_character_count(text).items():
        print(f"'{char}': {count}")
    print ("============= END ===============")