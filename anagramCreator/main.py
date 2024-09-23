#Samuel Andelin, Raid: Anagram Creator
import random
def makeanagram(word):
    listforswitching = []
    for i in word:
        listforswitching.append(i)
        switchedlist = []
    for i in listforswitching:
        switchedlist.insert(random.randint(0, len(listforswitching)), i)
    anagram = "".join(switchedlist)
    return anagram
wordforanagram = input("Input a word for anagram generator: ")
print("First anagram: "+makeanagram(wordforanagram))
print("Second anagram: "+makeanagram(wordforanagram))
print("Third anagram: "+makeanagram(wordforanagram))
print("Fourth anagram: "+makeanagram(wordforanagram))
print("Fifth anagram: "+makeanagram(wordforanagram))