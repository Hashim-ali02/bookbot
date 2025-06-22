def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    count = {}
    for char in text:
        char = char.lower()
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1
    return count
    
def sort_on(items):
    return items["num"]

def sort_character_dict(char_dict):
    char_list = []
    for char in char_dict:
        if char.isalpha():
            char_list.append({"char": char, "num": char_dict[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
