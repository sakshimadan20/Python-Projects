# to create a new encryption algorithm

def convert_to_binary (decimal):
    bitstring = ''
    while(decimal > 0):
        decimal = decimal // 2
        remainder = decimal % 2
        bitstring = str(remainder) + bitstring
    return bitstring
    
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

input_string = input("Enter the string: ")

ascii_list = []
binary_string = ""

for char in input_string:
    ascii_list.append(ord(char) + 1)

for ascii in ascii_list:
    converted_ascii = convert_to_binary(ascii)
    print(ascii, converted_ascii)
    binary_string = binary_string + converted_ascii

print(binary_string, len(binary_string))
print("Encrypted bitstring is:", shift_left(binary_string,''))
    
