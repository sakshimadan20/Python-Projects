# Function to calculate square root of a number

def Newton(n):
    estimate = 1.0
    tolerance = 0.000001
    
    while(True):
        estimate = (estimate + n / estimate) / 2
        difference = abs(n - estimate ** 2)
        if (difference <= tolerance):
            break
        
    return(estimate)
    
def main():
    while(True):
        number = float(input("Enter a positive number: "))
        print(Newton(number))
    
main()