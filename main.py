def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)#getting the text from the filepath
    word_count = num_of_words(text)#getting how much words are in the book
    dict_of_letters = count_characters(text)#getting a dict of how much each letter appears in the book
    chars_sorted_list = dict_of_letters_to_sorted_list(dict_of_letters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words were found in this document")
    print(

    )
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End Report ---")


def get_book_text(path): #gets the text using the filepath
    with open(path) as f:
        return f.read()

def num_of_words(text): #gets the amount of words in the book
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1
    return word_count

def count_characters(text): #gives a dict saying how many times each letter appears in the book
    lowered_text = text.lower()
    dict_of_letters = {}
    chars = []
    for letter in lowered_text: #adding each letter to the chars list
        chars.append(letter)
    for char in chars: #every letter in text is now in chars, so the first time
        if char in dict_of_letters: #a letter appears, the value is set to 1, then 
            dict_of_letters[char] += 1 #all the other times, 1 is added to the value
        else:
            dict_of_letters[char] = 1
    return dict_of_letters

def sort_on(d):
    return d["num"]

def dict_of_letters_to_sorted_list(num_chars_dict): #returns a sorted list of dicts with each dict having the character and how much times it appears
    sorted_list = []
    for char in num_chars_dict:
        sorted_list.append({"char": char, "num": num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()
