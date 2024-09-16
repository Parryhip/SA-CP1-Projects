#Samuel Andelin, Fibonnaci Sequence Generator
howmanynumbers = int(input("How many numbers of the fibonacci sequence should I generate?: "))
numbercount = 0
printinglist = []
a = 0
b = 1
c = 1
while numbercount <= howmanynumbers:
    printinglist.append(a)
    a = b + c
    numbercount += 1
    if numbercount == howmanynumbers:
        break
    printinglist.append(b)
    b = a + c
    numbercount += 1
    if numbercount == howmanynumbers:
        break
    printinglist.append(c)
    c = a + b
    numbercount += 1
    if numbercount == howmanynumbers:
        break
printinglisttostring = "".join(str(printinglist))
print(str(printinglisttostring))


