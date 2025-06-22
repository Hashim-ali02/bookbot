import sys
from stats import count_words, count_characters, sort_character_dict

def get_book_text(filepath):
     with open(filepath) as book:
        return book.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = count_words(text)
    count = count_characters(text)
    sorted_list = sort_character_dict(count)
    print("============ BOOKBOT ============") 
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_list:
        print(f"{char["char"]}: {char["num"]}") 

main()  