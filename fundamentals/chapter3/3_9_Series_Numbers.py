#Program to take the series of numbers as input & find sum and average of the numbers

mylist = input("Enter your list separated by comma and press enter to finish: ")    
mylist = mylist.strip()

sum = 0    
count = 0

for number in mylist.split(","):
    print(":" + number + ":")
    number = number.strip()
    print(":" + number + ":")
    if(number == ""):
        continue
    count += 1
    sum += int(number)

print("The sum of the numbers is: " + str(sum))
print("The average of the numbers is: " + str(sum/count))