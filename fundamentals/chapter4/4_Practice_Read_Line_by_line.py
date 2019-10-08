#Comparing 2 files line by line

import os

filename1 = input("Enter file 1: ")
filename2 = input("Enter file 2: ")

f1 = open(filename1, 'r')
f2 = open(filename2, 'r')

if (os.path.exists(filename1) == True) & (os.path.exists(filename2) == True):
    for line_filename1 in f1:
        if(line_filename1 == f2.readline()):
            continue
        else:
            print("No")
            print(line_filename1)
            break
            


    
        
                
        
    