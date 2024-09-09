#Samuel Andelin, Palindrome
palindrome = input("Enter a string to check if it is a palindrome: ")
palindrome = palindrome.lower()
list = []
for i in palindrome:
    list.append(i)
revlist = reversed(list)
rev = "".join(revlist)

if str(rev) == str(palindrome):
    print("This is a palindrome!")
else:
    print("This isn't a palidrome.")