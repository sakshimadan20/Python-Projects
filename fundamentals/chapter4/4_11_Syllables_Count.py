# to count the syllables 

sentence = input("Enter the text file: ")
vowels = "aeiou"
count = 0
flag = 0
sentence_list = sentence.split()

for word in sentence_list:
    flag = 0
    for char in word:
        if flag == 1:
           flag = 0
           
        elif char in vowels:
             flag = 1
             count += 1
             
    if word.endswith('es') == True or word.endswith('ed') == True or word.endswith('e') == True:
        count -= 1
    if word.endswith('le') == True:
        count += 1
            
print(count)