def myRange(stop, start = None, step = None):
    if (start == None):
        return myRange_start_to_stop(0, stop, step)
    else:
        return myRange_start_to_stop(stop, start, step)
    
def myRange_start_to_stop(start, stop, step = None):
    if (step == None):
        step = 1
    
    lyst = []
    while start < stop:
        lyst.append(start)
        start += step
        
    return(lyst)
                
def main():
    print(myRange(6,12,3))
    
main()
