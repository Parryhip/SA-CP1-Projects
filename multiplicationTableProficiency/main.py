#Samuel Andelin, Proficiency Test for Multiplication Table
multiplesinput = input("What number should I make multiples of till 12?:") 
multipleslist = []
for i in range(0,13):
    multipleslist.append(str(int(multiplesinput)*i))
strlist = ", ".join(multipleslist)
print("Here are your numbers: "+ strlist)