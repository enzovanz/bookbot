def get_num_words(string):
    return len(string.split())

def get_char_count(string):
    char_count_dict = {}
    for char in string.lower():
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1 
    return char_count_dict

def get_dict_to_dict_list(dict):
    output_list = []
    for key in dict:
        temp_dict = {}
        temp_dict["char"] = key
        temp_dict["num"] = dict[key]
        output_list.append(temp_dict)
    output_list.sort(reverse=True, key=lambda x: x["num"])
    return output_list

def get_book_text(filepath):
    with open(filepath) as file:
        content = file.read()
    return content

if __name__ == "__main__":
    test = {'t': 29493, 'h': 19176, 'e': 44538, ' ': 70480, 'p': 5952, 'r': 20079, 'o': 24494, 'j': 497, 'c': 9011, 'g': 5795, 'u': 10111, 'n': 23643, 'b': 4868, 'k': 1661, 'f': 8451, 'a': 25894, 's': 20360, 'i': 23927, ';': 1350, ',': 5962, 'm': 10206, 'd': 16318, '\n': 7628, 'y': 7756, 'w': 7450, 'l': 12306, 'v': 3737, '.': 3121, '-': 173, ':': 211, '2': 19, '3': 15, '0': 18, '1': 91, '[': 2, '#': 1, '4': 12, '5': 12, ']': 2, '&': 5, '8': 24, '/': 8, '*': 97, '’': 144, 'x': 691, '_': 124, 'q': 325, '?': 208, '—': 123, '6': 9, 'z': 235, '(': 35, ')': 35, '7': 18, 'æ': 28, '!': 201, '“': 506, '”': 316, '9': 9, 'ë': 2, '‘': 43, 'â': 8, 'ê': 7, 'ô': 1, '™': 57, '•': 4, '%': 1, '$': 2}
    print(get_dict_to_dict_list(test))
