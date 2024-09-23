#Samuel Andelin, Secret Cypher
def shift(word):
    newword = []
    for i in word:
        if i == "a":
            newword.append("b")
        elif i == "b":
            newword.append("c")
        elif i == "c":
            newword.append("d")
        elif i == "d":
            newword.append("e")
        elif i == "e":
            newword.append("f")
        elif i == "f":
            newword.append("g")
        elif i == "g":
            newword.append("h")
        elif i == "h":
            newword.append("i")
        elif i == "i":
            newword.append("j")
        elif i == "j":
            newword.append("k")
        elif i == "k":
            newword.append("l")
        elif i == "l":
            newword.append("m")
        elif i == "m":
            newword.append("n")
        elif i == "n":
            newword.append("o")
        elif i == "o":
            newword.append("p")
        elif i == "p":
            newword.append("q")
        elif i == "q":
            newword.append("r")
        elif i == "r":
            newword.append("s")
        elif i == "s":
            newword.append("t")
        elif i == "t":
            newword.append("u")
        elif i == "u":
            newword.append("v")
        elif i == "v":
            newword.append("w")
        elif i == "w":
            newword.append("x")
        elif i == "x":
            newword.append("y")
        elif i == "y":
            newword.append("z")
        elif i == "z":
            newword.append("a")
        elif i == " ":
            newword.append(" ")
    newwordstr = "".join(newword)
    return newwordstr
wordtochange = input("Choose a message to be coded(all lowercase): ")
print("Original word: " + wordtochange) 
print("New word: " + shift(wordtochange))