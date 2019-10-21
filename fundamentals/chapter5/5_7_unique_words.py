# Program to print the unique words in the file in alphabetical order

filename = input("Enter the file name: ")
word_list =[]

f = open(filename, 'r')

for line in f:
    line = line.split()
    for word in line:
        if word.lower() in word_list:
            continue
        else:
            word_list.append(word.lower())
            
print(sorted(word_list))
        