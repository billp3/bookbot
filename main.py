def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = count_chars(text)
    char_counts_sorted = dict(sorted(char_counts.items(), key=lambda item: item[1], reverse=True))

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    
    for c in char_counts_sorted:
        if c.isalpha():
            print(f"The '{c}' character was found {char_counts_sorted[c]} times")
    
    print(f"--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def count_chars(text):
    text = text.lower()
    chars = {}
    for char in text:
        if char not in chars:
            chars[char] = 0
        chars[char] += 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

