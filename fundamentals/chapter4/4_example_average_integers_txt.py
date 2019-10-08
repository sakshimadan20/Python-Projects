#to find the average of integers from a .txt file

f = open("integers.txt", 'r')
sum_num = 0
count = 0
for line in f:
    line = line.split()
    #line = int(line)
    for number in line:
        number = int(number)
        count += 1
        sum_num += number
        
print("Average of numbers is: ", sum_num/count)
        