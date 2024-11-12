#Samuel Andelin, Password Validator\
specialcharacters = ["~", "`", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", "\\", "|", ":", ";", "'", '"', "<", ">", ",", ".", "?", "/"]
numberscount = 0
passwordvalidated = False
while passwordvalidated == False:
    newpassword = input("What is your password?")
    for i in specialcharacters:
        if i not in newpassword:
            print("No special characters in password!")
            break
        else:
            pass
    for i in newpassword:
        try:
            test = int(i)
            numberscount += 1
        except:
            continue
    if numberscount == 0:
        print("No numbers in password!")
        continue
    if len(newpassword) < 8:
        print("Password is not long enough!")
        continue
    else:
        passwordvalidated = True
print("Password validated!")