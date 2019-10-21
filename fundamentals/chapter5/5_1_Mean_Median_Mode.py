def func_mean(number_list):
    
    sum_numbers = 0
    count = 0
    for number in number_list:
        count += 1
        sum_numbers += float(number)
        
    mean_numbers =  round(float(sum_numbers/count),2)
    return(mean_numbers)    
    
def func_median(number_list):
    
    length = len(number_list)
    if(length % 2 == 0):
        median_numbers = (float(number_list[length // 2]) + float(number_list[(length // 2) - 1])) / 2
    else:
        median_numbers = number_list[(length // 2)]
        
    return(median_numbers)

def func_mode(number_list):
    
    dictionary = {}
    mode_list = []
    for number in number_list:
        if (dictionary.get(number,None) == None):
            dictionary[number] = 1
        else:
            dictionary[number] = dictionary[number] + 1
            
    maximum_value = 0
    for key in dictionary:
        if (dictionary[key] > maximum_value):
            maximum_value = dictionary[key]
    
    for key in dictionary:
        if (dictionary[key] == maximum_value):
            mode_list.append(key)
            
    return(mode_list)
    
def main():
    values_list =[]
    values = input("Enter the list of values separated by comma: ")
    for value in values.split(','):
        values_list.append(value)
    print(func_mean(values_list))
    print(func_median(values_list))
    print(func_mode(values_list))

# The entry point for program execution
main()

    

