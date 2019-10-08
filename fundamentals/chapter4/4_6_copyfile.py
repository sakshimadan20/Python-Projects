# to read from one file and write to another

file1 = input("Enter the file name 1: ")
file2 = input("Enter the file name 2: ")

f1 = open(file1, 'r')
f2 = open(file2, 'w')

f1 = f1.read()
f2.write(f1)

f2.close()

