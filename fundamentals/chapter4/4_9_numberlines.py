# to read from one file and write to another line by line

file1 = input("Enter the file name 1: ")
file2 = input("Enter the file name 2: ")

f1 = open(file1, 'r')
f2 = open(file2, 'w')

count = 1

for line in f1:
    line2 = '%4s> %s' % (count, line)
    f2.write(line2)
    count += 1

f2.close()