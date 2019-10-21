# Function to calculate square root of a number

def Newton(n, estimate):
    
    tolerance = 0.000001
    estimate = (estimate + n / estimate) / 2
    difference = abs(n - estimate ** 2)
    if (difference <= tolerance):
        return(estimate)
    else:
        return(Newton(n, estimate))
            
def main():
    while(True):
        number = float(input("Enter a positive number: "))
        print(Newton(number, 1.0))
    
main()