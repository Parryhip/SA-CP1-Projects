#Samuel Andelin, Password Validator\
specialcharacters = ["~", "`", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", "\\", "|", ":", ";", "'", '"', "<", ">", ",", ".", "?", "/"]
numberscount = 0
specialchar = 0
while True:
    numbersinpassword = False
    passwordlongenough = False
    specialchar = 0
    newpassword = input("What is your password?")
    for i in specialcharacters:
        if i in newpassword:
            specialchar += 1
        else:
            continue
    for i in newpassword:
        try:
            test = int(i)
            numberscount += 1
        except:
            continue
    if numberscount == 0:
        print("No numbers in password!")
        numbersinpassword = False
    else:
        numbersinpassword = True
    if len(newpassword) < 8:
        print("Password is not long enough!")
        passwordlongenough = False
    else:
        passwordlongenough = True
    if specialchar == 0:
        print("No special characters in password.")
        continue
    else:
        pass
    if numbersinpassword == False:
        continue
    else:
        pass
    if passwordlongenough == False:
        continue
    else:
        break

print("Password validated!")