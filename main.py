import sys

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_report(book_path, text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def each_word_count(text):
    word_count = {}
    for word in text:
        lowercase_word = word.lower()
        if lowercase_word in word_count:
            word_count[lowercase_word] += 1
        else:
            word_count[lowercase_word] = 1
    return word_count

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(word_dict):
    sorted_list = []
    for ch in word_dict:
        sorted_list.append({"char": ch, "num": word_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def print_report(book_path, text):
    print(f"--- Begin report of {book_path} ---")
    total_words_count = count_words(text)
    print(f"{total_words_count} words found in the document")
    word_dict = each_word_count(text)
    sorted_char_count_list = chars_dict_to_sorted_list(word_dict)
    for item in sorted_char_count_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End Report ---")
   
main()