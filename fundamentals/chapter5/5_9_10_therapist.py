import random

hedges = ("Please tell me more.", "Many of my patients tell me the same thing. ", "Please continue.")
qualifiers = ("Why do you say that ", "You seem to think that ","Can you explain why ")
replacements = {"I":"you", "me":"you", "my":"your", "we":"you", "us":"you", "mine":"yours", "am":"are", "you":"I", "are":"am"}

def reply(sentence, history_list):    
    probability = random.randint(1, 4)
    if probability == 1:
        return random.choice(hedges)
    elif probability == 2 and len(history_list) > 3:
        return("Earlier you said that ") + changePerson(random.choice(history_list[0:len(history_list)-3]))
    else:
        return random.choice(qualifiers) + changePerson(sentence)
        
def changePerson(sentence):
    replyWords = []
    words = sentence.split()
    for word in words:
        replyWords.append(replacements.get(word, word))
    return " ".join(replyWords)

def main():
    history_list = []
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print("Have a nice day!")
            break
        print(reply(sentence, history_list))
        history_list.append(sentence)
        
main()
        
