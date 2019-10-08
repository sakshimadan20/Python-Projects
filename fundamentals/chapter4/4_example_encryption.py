#Encryption

plainText = input("Enter a lowercase one-word: ")
distance = int(input("Enter the distance value: "))
code = ""

for char in plainText:
    encrypt = ord(char) + distance
    if encrypt > 122:
       encrypt = encrypt - 26
    code += chr(encrypt)

print("\nEncypted word is: " + code)
   
