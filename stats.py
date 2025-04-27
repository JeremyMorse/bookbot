def get_word_count(text):
    words = []
    words = text.split()
    count = len(words)
    return count

def get_char_count(text):
    chars = {}
    for i in text:
        i = i.lower()
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    return chars

def get_sorted_chars(chars_dict):
    sorted_chars = []
    for char in chars_dict:
        split_dict = {"char": char, "num": chars_dict[char]} 
        sorted_chars.append(split_dict)
    sorted_chars.sort(reverse=True, key=lambda dict: dict["num"])
    return sorted_chars
