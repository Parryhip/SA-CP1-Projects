#Samuel Andelin, Simple Histogram
inputs = int(input("How many inputs do you have?: "))
inputs += 1
inputslist = []
for i in range(inputs-1):
    inputtopush = int(input("What is the input?: "))
    inputslist.append(inputtopush)
    print("Recorded!")
for i in range(inputs-1):
    print(str(i+1)+": ")
    print("*"*inputslist[i])