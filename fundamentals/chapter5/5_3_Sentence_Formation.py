import random

def getwords(filename):
    temp_list = []
    f = open(filename, 'r')
    for line in f:
        line = line.split() 
        for word in line:
            temp_list.append(word)
    return(tuple(temp_list))
    
articles = getwords("articles.txt")
nouns = getwords("nouns.txt")
verbs = getwords("verbs.txt")
prepositions = getwords("prepositions.txt")


def sentence():
    return nounPhrase() + " " + verbPhrase()
    
def nounPhrase():
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()
    
def prepositionalPhrase():
    return random.choice(prepositions) + " " + nounPhrase()
    
def main():
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())
               
main()
    
    
    
    
    

