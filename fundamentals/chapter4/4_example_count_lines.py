f = open("integers.txt", 'r')
count = 0
for line in f:
    if(line ==""):
        break
    count += 1
print(count)
        
