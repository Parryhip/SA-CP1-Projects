#Samuel Andelin, Pig Latin Converter
def switch(word):
    newword = []
    if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
        newword.append(word)
        newword.append("way")
    else:
        if word.find("a") != -1:
            index = word.find("a")
            newword.append(word[index:])
            newword.append("ay")
        elif word.find("e") != -1:
            index = word.find("e")
            newword.append(word[index:])
            newword.append("ay")
        elif word.find("i") != -1:
            index = word.find("i")
            newword.append(word[index:])
            newword.append("ay")
        elif word.find("o") != -1:
            index = word.find("o")
            newword.append(word[index:])
            newword.append("ay")
        elif word.find("u") != -1:
            index = word.find("u")
            newword.append(word[index:])
            newword.append("ay")
    return newword
wordtochange = input("What word should I switch to piglatin?")
newword = switch(wordtochange)
print(newword)
newwordtostring = "".join(newword)
print(newwordtostring)