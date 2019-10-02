# Tabulate the Salary of a teacher based on the number of years

#input the values
salary = float(input("Enter the first year salary: "))
perc_salary = float(input("Enter the % salary increase: "))
years = int(input("Enter the number of years: "))

i=0

#creating table header
print("\n%8s%18s" % ("Year", "Salary"))

while(i < years):
    i+=1
    print("%8d%18.2f" % (int(i), float(salary)))
    salary = salary + ((perc_salary/100) * salary)