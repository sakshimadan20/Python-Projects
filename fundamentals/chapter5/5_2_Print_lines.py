import sys

filename = input("Enter the name of the file: ")
f = open(filename,'r')
count = 0
for line in f:
    count += 1
    
print("\nThe number of lines in the file are: " + str(count))

line_number = int(input("Enter the line number you want to print: "))
if (line_number == 0):
    sys.exit()

f = open(filename, 'r')
line_count = 0

for line in f:
    line_count += 1
    if(line_count == line_number):
        print(line)

    
    