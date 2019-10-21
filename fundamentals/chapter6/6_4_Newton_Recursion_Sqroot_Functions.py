# Function to calculate square root of a number

def improveEstimate(n, estimate = 1.0):
    estimate = (estimate + n / estimate) / 2
    return(estimate)

def limitReached(n, estimate):
    difference = abs(n - estimate ** 2)
    return(difference)
   
def Newton(n, estimate = 1.0):
    tolerance = 0.000001
    estimate = improveEstimate(n, estimate)
    difference = limitReached(n, estimate)
    if (difference <= tolerance):
        return(estimate)
    else:
        return(Newton(n, estimate))
            
def main():
    while(True):
        number = float(input("Enter a positive number: "))
        print(Newton(number))
    
main()