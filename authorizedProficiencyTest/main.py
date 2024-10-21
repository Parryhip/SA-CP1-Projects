#Samuel Andelin, Authorized Proficiency Test
authorizedusers = ["Patty", "John", "Aaron", "Jerry", "Jimmy", "George", "Tim", "Fred"]
authorizedadmins = ["Bobby", "Bossy"]
nameofuser = input("What is your name? (capitalize it!): ")
if nameofuser in authorizedusers:
    print("You are a user.")
elif nameofuser in authorizedadmins:
    print("You are an admin.")
else:
    print("You are not authorized.")