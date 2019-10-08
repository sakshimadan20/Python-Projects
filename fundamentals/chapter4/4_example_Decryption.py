#Decryption

codedWord = input("Enter the coded word: ")
distance = int(input("Enter the distance value: "))
plainText = ""

for char in codedWord:
    decrypt = ord(char) - distance
    if decrypt < 97:
        decrypt = decrypt + 26
    plainText = plainText + chr(decrypt)

print("\nPlain Text word is: " + plainText)
   
