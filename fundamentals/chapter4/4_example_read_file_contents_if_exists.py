#to read the contents of the file if it exists

import os

file_name = input("Enter the file name to be checked: ")

if os.path.isfile(file_name):
    
    f = open(file_name, 'r')
    print(f.read())

else:
    
    print("Path Incorrect")    
