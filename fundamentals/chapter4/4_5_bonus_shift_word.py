sentence = input("Enter a sentence: ")

def shift_left (string, separator):

    if separator == '':
        string_list = list(string)
    else:
        string_list = string.split(separator)
    
    length = len(string_list)
    first = string_list[0]

    for i in range(0, length-1) :
        string_list[i] = string_list[i + 1]

    string_list[length - 1] = first 
    return (separator.join(string_list))

print(shift_left(sentence, ' '))