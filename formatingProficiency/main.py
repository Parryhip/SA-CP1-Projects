#Samuel Andelin, What are these numbers? 
usernum = input("Input a number to have commas in-between every thousand, \nbe rounded to the nearest ten thousandth, \nbe a percentage, \nand be a dollar amount.")
commasint = f"{float(usernum):,}"
print("\nYour number with commas is "+ str(commasint))
print("\nYour number rounded to the nearest ten thousand is "+ str(round(float(usernum), 4)))
percentagenum = float(usernum)*100
print("\nYour number as a percentage is "+str(percentagenum)+" %")
dollarnum = "$" + str(round(float(usernum), 2))
print("\nYour number as a dollar amount is "+dollarnum)