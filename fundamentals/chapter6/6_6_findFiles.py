import os, os.path

QUIT = '7'
COMMANDS = ('1','2','3','4','5','6','7','8')
MENU = """ 1 List the current directory
2 Move up
3 Move down
4 Number of files in the directory
5 Size of the directory in bytes
6 Search for a filename
7 View the contents of a file
8 Quit the program"""

def main():
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == '8':
            print("Have a nice day!")
            break
            
def acceptCommand():
    command = input("Enter a number: ")
    if command in COMMANDS:
        return command
    else:
        print("Error: Command not recognized")
        return acceptCommand()
        
def runCommand(command):
    if command == '1':
        listCurrentDir(os.getcwd())
    elif command == '2':
        moveUp()
    elif command == '3':
        moveDown(os.getcwd())
    elif command == '4':
        print(countFiles(os.getcwd()))
    elif command == '5':
        print(countBytes(os.getcwd()))
    elif command == '6':
        target = input("Enter the search string: ")
        fileList = findFiles(target, os.getcwd())
        if not fileList:
            print("String not found")
        else:
            for f in fileList:
                print(f)
    elif command == '7':
        fileList = fileContent(os.getcwd())
        if fileList == '':
            print("No files in the directory")
        else:
            for files in fileList: print(files)
            fileName = input("Enter the name of the file to be read: ")
            findFiles(fileName, os.getcwd())
            
                
def listCurrentDir(dirName):
    lyst = os.listdir(dirName)
    for element in lyst: print(element)
    
def moveUp():
    os.chdir("..")
    
def moveDown(currentDir):
    newDir = input("Enter the directory name: ")
    if os.path.exists(currentDir + os.sep + newDir) and os.path.isdir(newDir):
        os.chdir(newDir)
    else:
        print("ERROR: no such name")
    
def countFiles(path):
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += 1
        else:
            os.chdir(element)
            count += countFiles(os.getcwd())
            os.chdir("..")
    return count
    
def countBytes(path):
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += os.path.getsize(element)
        else:
            os.chdir(element)
            count += countBytes(os.getcwd())
            os.chdir("..")
    return count
    
def findFiles(target, path):
    files = []
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            if target in element:
                files.append(path + os.sep + element)
        else:
            os.chdir(element)
            files.extend(findFiles(target, os.getcwd()))
            os.chdir("..")
    return files
    
def fileContent(path):
    files = []
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            files.append(element)
        else:
            os.chdir(element)
            files.extend(fileContent(os.getcwd()))
            os.chdir("..")
            
    return files
    
main()
                
        
    
            
        
    