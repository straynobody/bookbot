import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
from stats import count_words, count_characters, frequency
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    character_counts = count_characters(text)
    sorted_characters = frequency(character_counts)
    print(f"Found {num_words} total words")
    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")
if __name__ == "__main__":
    main()
