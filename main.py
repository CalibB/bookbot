def main():
    with open("./books/frakenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)
    
    # print(count_words(file_contents))
    # print(count_characters(file_contents))

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
    

def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    
    return count

def count_characters(text):
    sanitized_text = text.lower()
    char_count = {}
    for char in sanitized_text:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    
    return char_count

main()