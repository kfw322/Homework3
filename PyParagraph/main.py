import os

sentences = []
words = []
endpunctuation = ["!","?","."]
otherpunctuation = [",",":","'","-"]
senstr = ""
totalchar = 0
totalwords = 0
totalsentences = 0

filepath=os.path.join("Resources","input.txt")

with open(filepath) as txtin:
    for word in txtin.read().split():
        totalwords += 1
        if any(string in endpunctuation for string in word):
            word = list(word)
            word = str(''.join([s for s in word if not s in endpunctuation]))
            words.append(word)
            senstr = " ".join(words)
            words=[]
            totalsentences += 1
            
        else:
            word = list(word)
            word = str(''.join([s for s in word if not s in otherpunctuation]))
            words.append(word) 
        totalchar += len(word)
            

    print("PARAGRAPH ANALYSIS")
    print("Total words:        " + str(totalwords))
    print("Total sentences:    " + str(totalsentences))
    print("Letters per word:   " + str(totalchar / totalwords))
    print("Words per sentence: " + str(totalwords / totalsentences))
