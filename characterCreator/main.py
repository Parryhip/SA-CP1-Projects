#Samuel Andelin, Character Creator RAID
print("Create your character!")
normal_dude = {
    "health": "30",
    "strength": "20",
    "dexterity": "15",
    "intelligence": "20"
}
wizard = {
    "health": "35",
    "strength": "10",
    "dexterity": "20",
    "intelligence": "40"
}
buff_dude = {
    "health": "40",
    "strength": "30",
    "dexterity": "5",
    "intelligence": "10"
}
name = input("What is your character's name?")
classs = input("What is your character's class(n for normal dude/w for wizard/b for buff dude)?")
if classs == "n":
    actual_class = "normal dude"
    health = normal_dude["health"]
    strength = normal_dude["strength"]
    dexterity = normal_dude["dexterity"]
    intelligence = normal_dude["intelligence"]
elif classs == "w":
    actual_class = "wizard"
    health = wizard["health"]
    strength = wizard["strength"]
    dexterity = wizard["dexterity"]
    intelligence = wizard["intelligence"]
elif classs == "b":
    actual_class = "buff dude"
    health = buff_dude["health"]
    strength = buff_dude["strength"]
    dexterity = buff_dude["dexterity"]
    intelligence = buff_dude["intelligence"]
else:
    actual_class = "piece of dirt"
    health = "0"
    strength = "0"
    dexterity = "0"
    intelligence = "0"
race = input("What is your character's race?(h for human/e for elf/d for dwarf)")
if race == "h":
    actual_race = "human"
    intelligenceint = int(intelligence)
    dexterityint = int(intelligence)
    strengthint = int(strength)
    healthint = int(health)
    intelligenceint += 5
elif race == "e":
    actual_race = "elf"
    intelligenceint = int(intelligence)
    dexterityint = int(intelligence)
    strengthint = int(strength)
    healthint = int(health)
    dexterityint += 5
elif race == "d":
    actual_race = "dwarf"
    intelligenceint = int(intelligence)
    dexterityint = int(intelligence)
    strengthint = int(strength)
    healthint = int(health)
    strengthint += 5
else:
    actual_race = "dirty"
    intelligenceint = int(intelligence)
    dexterityint = int(intelligence)
    strengthint = int(strength)
    healthint = int(health)
print("Your player's name is "+name+".")
print("Your player's class is "+actual_class+".")
print("Your player's race is "+actual_race+".")
print("Your player's health is "+str(healthint)+".")
print("Your player's strength is "+str(strengthint)+".")
print("Your player's dexterity is "+str(dexterityint)+".")
print("Your player's intelligence is "+str(intelligenceint)+".")