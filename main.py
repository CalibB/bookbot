from stats import count_characters, count_words, sorted_dict
import sys

def main():
    with open(f"{sys.argv[1]}") as f:
        file_contents = f.read()

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z']

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(file_contents)} total words")
    print("--------- Character Count -------")

    file_char_dict = count_characters(file_contents)
    letter_list = sorted_dict(file_char_dict)

    for dict in letter_list:
        if dict['char'] in alphabet:
            print(f"{dict['char']}: {dict['num']}")

    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()
