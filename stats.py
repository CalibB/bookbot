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


def sort_on(dict):
    return dict["num"]


def sorted_dict(dict):
    letters = []
    for key in dict:
        unsort_letters = {
            "char": key,
            "num": int(dict[key])
        }
        letters.append(unsort_letters)

    letters.sort(reverse=True, key=sort_on)
    return letters
