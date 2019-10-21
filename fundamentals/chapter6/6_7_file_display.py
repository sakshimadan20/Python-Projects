import os
import os.path

def findFiles(link):
    if os.path.isfile(link) == True:
        print(" :::::::::::::::::: " + str(link) + " ::::::::::::::::::::::::::: ")
        f = open(link, 'r')
        for line in f:
            print(line)
    else:
        os.chdir(link)
        lyst = os.listdir(link)
        print("Directory found: " + str(lyst))
        for files in lyst:
            findFiles(os.getcwd() + os.sep + files)
        os.chdir('..')
    
def main():
    findFiles('/Users/sakshi/Documents/Python/Python-Projects/fundamentals/chapter6')

main()