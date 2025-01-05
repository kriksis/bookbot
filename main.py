def get_num_words(text):
    world = text.split()
    return len(world)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} total words")
    
    chars_dict = get_chars_dict(text)
    print(chars_dict)



main()
