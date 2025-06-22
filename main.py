from stats import count_words, count_characters, sort_character_dict

def get_book_text(filepath):
     with open(filepath) as book:
        return book.read()

def main():
    text = get_book_text("./books/frankenstein.txt")
    num_words = count_words(text)
    count = count_characters(text)
    sorted_list = sort_character_dict(count)
    print("============ BOOKBOT ============") 
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_list:
        print(f"{char["char"]}: {char["num"]}") 

main()  