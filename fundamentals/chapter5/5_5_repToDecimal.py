dictionary = {'A':'10', 'B':'11','C':'12','D':'13','E':'14','F':'15'}

def repToDecimal(binary, base):
    binary_list = binary.split()
    decimal = 0
    length = len(binary_list) - 1
    for number in binary_list:
        for char in range(length, -1, -1):
            decimal = decimal + (int(binary_list[length - char]) * (base ** char))
        return(decimal)

def main():
    binary_string =''
    binary = input("Enter the binary digits: ")
    for digit in binary:
        value = dictionary.get(digit,digit)
        binary_string += value + " "
    print(repToDecimal(binary_string,2))
    print(repToDecimal(binary_string,8))
    print(repToDecimal(binary_string,16))

main()
    
        
        
    