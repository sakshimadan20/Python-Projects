def isSorted(lyst):
    len_lyst = len(lyst)
    decision = True
    
    if(len_lyst < 2):
        return(decision)
        
    for count in range(0, len_lyst - 1):
        if(lyst[count] > lyst[count + 1]):
            decision = False
            break
    
    return(decision)
    
def main():
    lyst = []
    print(isSorted(lyst))
    lyst = [1]
    print(isSorted(lyst))
    lyst = list(range(10))
    print(isSorted(lyst))
    lyst[9] = 3
    print(isSorted(lyst))
main()