def main():
    with open("./books/frakenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)
    
    # print(count_words(file_contents))
    print(count_characters(file_contents))
    

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