#to count number of 4 letter words in a .txt file

f = open("example.txt", 'r')
count = 0
for line in f:
    line = line.split()
    for word in line:
        if len(word) == 4:
            count += 1
print(count)
    
#these are the words in example.txt as of now
#("saks sahe ab sakshi gesu sachin saheb")
