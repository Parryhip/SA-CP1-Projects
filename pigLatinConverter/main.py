#Samuel Andelin, Pig Latin Converter
def switch(word):
    newword = []
    if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
        newword.append(word)
        newword.append("way")
    else:
        wordlist = []
        for i in word:
            wordlist.append(i)
        while wordlist[0] != "a" or wordlist[0] != "e" or wordlist[0] != "i" or wordlist[0] != "o" or wordlist[0] != "u":
            wordlist.append(word[0])
            del wordlist[0]
            newword.append(word)
            newword.append("ay")
    return newword
wordtochange = input("What word should I switch to piglatin?")
newword = switch(wordtochange)
print(newword)
newwordtostring = "".join(newword)
print(newwordtostring)