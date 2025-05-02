from stats import count_characters, count_words

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z']

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document\n")

    file_char_dict = count_characters(file_contents)

    for char in file_char_dict:
        if char in alphabet:
            print(f"The '{char}' character was found {file_char_dict[char]} times'")

    print("--- End report ---")


main()
