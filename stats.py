def count_words(text):
    words = text.split()
    return len(words)
def count_characters(text):
    text = text.lower()
    char_count = {}
    for character in text:
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1
    return char_count
def frequency(char_dict):
    sorted_char = []
    for char, num in char_dict.items():
        if char.isalpha():
            new_list = {"char": char, "num": num}
            sorted_char.append(new_list)
    sorted_char.sort(key=lambda x: x["num"], reverse=True)
    return sorted_char