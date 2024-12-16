#Samuel Andelin, FINAL PROJECT!!!
import random
import time
listofanamotopoeia = ["Bang!", "Whack!", "Kapow!", "Kazoinks!", "Bonk!", "Bazingha!", "Yooooowch!", "Oowie", "Boom! Shackalackalacka!"]
room1 = {
    'monster_probability' : 0,
    'final_boss' : False,
    'room_accesses' : [2, 3],
    'common_chest_prob' : 100,
    'rare_chest_prob' : 0,
    'legendary_chest_prob' : 0
}
room2 = {
    'monster_probability' : 50,
    'final_boss' : False,
    'room_accesses' : [4, 1],
    'common_chest_prob' : 70,
    'rare_chest_prob' : 30,
    'legendary_chest_prob' : 0
}
room3 = {
    'monster_probability' : 60,
    'final_boss' : False,
    'room_accesses' : [1, 6, 9],
    'common_chest_prob' : 40,
    'rare_chest_prob' : 40,
    'legendary_chest_prob' : 20
}
room4 = {
    'monster_probability': 60,
    'final_boss' : False,
    'room_accesses' : [2, 5],
    'common_chest_prob' : 60,
    'rare_chest_prob' : 40,
    'legendary_chest_prob' : 0
}
room5 = {
    'monster_probability' : 70,
    'final_boss' : False,
    'room_accesses' : [4, 7, 9],
    'common_chest_prob' : 49,
    'rare_chest_prob' : 50,
    'legendary_chest_prob' : 1
}
room6 = {
    'monster_probability' : 100,
    'final_boss' : False,
    'room_accesses' : [3],
    'common_chest_prob' : 10,
    'rare_chest_prob' : 20,
    'legendary_chest_prob' : 70
}
room7 = {
    'monster_probability' : 80,
    'final_boss' : False,
    'room_accesses' : [5, 8],
    'common_chest_prob' : 10,
    'rare_chest_prob' : 60,
    'legendary_chest_prob' : 30
}
room8 = {
    'monster_probability' : 90,
    'final_boss' : False,
    'room_accesses' : [7, 9],
    'common_chest_prob' : 0,
    'rare_chest_prob' : 50,
    'legendary_chest_prob' : 50
}
room9 = {
    'monster_probability' : 100,
    'final_boss' : True,
    'room_accesses' : [],
    'common_chest_prob' : 0,
    'rare_chest_prob' : 0,
    'legendary_chest_prob' : 100
}
plyrstats = {
    'hp' : 100,
    'strength' : 13,
    'speed' : 13,
    'potioninventory' : [],
    'spellinventory' : [],
    'weaponinventory' : [],
    'weaponcurrentlyequipped' : "dagger",
}
normal_enemy = {
    'hp' : 30,
    'strength' : 10,
    'speed' : 10
}
final_boss = {
    'hp' : 100,
    'strength' : 18,
    'speed' : 18,
    'inventory' : ['fireball', 'health potion', 'slow spell']
}
def play_again():
    while True:
        playagain = input("Do you want to play again?(y/n)")
        if playagain.lower() == "y":
            return True
        elif playagain.lower() == "n":
            return False
        else:
            print("Invalid input.")
            time.sleep(0.5)
            continue
def plyrturn():
    while True:
        plyraction = input("What do you want to do? 1 for attack with sword, 2 for cast spell, 3 for use potion, 4 for switch weapon, and 5 for run away.")
        if plyraction == "1":
            print("You attack with your sword.")
            time.sleep(0.5)
            print("Rolling die for attack...")
            time.sleep(1)
            attack = random.randint(1,20)
            print("You got a " + attack + ".")
            time.sleep(0.5)
            overall_attack = str((plyrstats['strength']//3)+attack)
            print("With your +"+ str(plyrstats['strength']//3) +" modifier means that you end with a "+overall_attack+".")
            time.sleep(0.5)
            print(random.choice[listofanamotopoeia])
            time.sleep(0.5)
            print("You hit the monster for "+overall_attack+".")
            normal_enemy['hp'] -= int(overall_attack)
            time.sleep(0.5)
            print("The monster's hp is now "+str(normal_enemy['hp'] +"."))
            time.sleep(0.5)
            if normal_enemy['hp'] <= 0:
                print("You killed the enemy!")
                return 'enemydead'
            else:
                print("Enemy's turn!")
                return 'enemynotdead'
        elif plyraction == "2":
            print("These are the potions that you have:")
            time.sleep(0.5)
            print(plyrstats['potioninventory'])
            time.sleep(0.5)
            while True:
                potiontouse = input("What potion do you want to use?(use the exact name of the item) or type exit to exit the potion menu.")
                if potiontouse in plyrstats['potioninventory']:
                    print("You use your" + potiontouse + ".")
                    if potiontouse == "speed potion":
                        speedpotionindex = plyrstats['potioninventory'].index("speed potion")
                        plyrstats['potioninventory'].pop(speedpotionindex)
                        plyrstats['speed'] += 5
                        return 'enemynotdead'
                    elif potiontouse == "strength potion":
                        strengthpotionindex = plyrstats['potioninventory'].index("strength potion")
                        plyrstats['potioninventory'].pop(strengthpotionindex)
                        plyrstats['strength'] += 5
                        return 'enemynotdead'
                    elif potiontouse == "health potion":
                        healthpotionindex = plyrstats['potioninventory'].index("health potion")
                        plyrstats['potioninventory'].pop(healthpotionindex)
                        plyrstats['hp'] += 20
                        return 'enemynotdead'
                elif potiontouse == "exit":
                    break
                else:
                    print("You do not have that potion!")
                    time.sleep(0.5)
        elif plyraction == "3":
            print("These are the spells that you have:")
            time.sleep(0.5)
            print(plyrstats['spellinventory'])
            time.sleep(0.5)
            while True:
                spelltouse = input("What spell do you want to use?(use the exact name of the item) or type exit to exit the spell menu.")
                if spelltouse in plyrstats['spellinventory']:
                    print("You use your" + spelltouse + ".")
                    if spelltouse == "fireball":
                        fireballspellindex = plyrstats['spellinventory'].index("fireball")
                        plyrstats['spellinventory'].pop(fireballspellindex)
                        normal_enemy['hp'] -= 20
                        print("You hit the monster for 20.")
                        time.sleep(0.5)
                        print("The monster's hp is now "+str(normal_enemy['hp'] +"."))
                        time.sleep(0.5)
                        if normal_enemy['hp'] <= 0:
                            print("You killed the enemy!")
                            return 'enemydead'
                        else:
                            print("Enemy's turn!")
                            return 'enemynotdead'
                    elif spelltouse == "slow spell":
                        slowspellspellindex = plyrstats['spellinventory'].index("slow spell")
                        plyrstats['spellinventory'].pop(slowspellspellindex)
                        normal_enemy['speed'] -= 10
                        print("You decrease the monster's speed by 10.")
                        time.sleep(0.5)
                        print("The monster's speed is now "+str(normal_enemy['speed'] +"."))
                        time.sleep(0.5)
                        return 'enemynotdead'
                elif spelltouse == "exit":
                    break
                else:
                    print("You do not have that spell!")
                    time.sleep(0.5)
        elif plyraction == "4":
            print("These are the weapons that you have:")
            print(plyrstats['weaponinventory'])
            time.sleep(0.5)
            print("The weapon currently equipped is your "+ plyrstats['weaponcurrentlyequipped']+".")
            time.sleep(0.5)
            while True:
                weapontoequip = input("What weapon do you want to equip?(use the exact name of the item) or type exit to exit the weapon menu.")
                if weapontoequip in plyrstats['weaponinventory']:
                    print("You equip your" + weapontoequip + ".")
                    if weapontoequip == "longsword":
                        if plyrstats['weaponcurrentlyequipped'] == "longsword":
                            plyrstats['strength'] -= 6
                        elif plyrstats['weaponcurrentlyequipped'] == "shortsword":
                            plyrstats['strength'] -= 4
                        elif plyrstats['weaponcurrentlyequipped'] == "dagger":
                            plyrstats['strength'] -= 2
                        plyrstats['weaponcurrentlyequipped'] = "longsword"
                        plyrstats['strength'] += 6
                    elif weapontoequip == "longsword":
                        if plyrstats['weaponcurrentlyequipped'] == "longsword":
                            plyrstats['strength'] -= 6
                        elif plyrstats['weaponcurrentlyequipped'] == "shortsword":
                            plyrstats['strength'] -= 4
                        elif plyrstats['weaponcurrentlyequipped'] == "dagger":
                            plyrstats['strength'] -= 2
                        plyrstats['weaponcurrentlyequipped'] = "shortsword"
                        plyrstats['strength'] += 4
                    elif weapontoequip == "dagger":
                        if plyrstats['weaponcurrentlyequipped'] == "longsword":
                            plyrstats['strength'] -= 6
                        elif plyrstats['weaponcurrentlyequipped'] == "shortsword":
                            plyrstats['strength'] -= 4
                        elif plyrstats['weaponcurrentlyequipped'] == "dagger":
                            plyrstats['strength'] -= 2
                        plyrstats['weaponcurrentlyequipped'] = "shortsword"
                        plyrstats['strength'] += 2
                elif weapontoequip == "exit":
                    break
                else:
                    print("You do not have that weapon!")
                    time.sleep(0.5)
        elif plyraction == "5":
            print("You try to run away.")
            monsterwantstoblock = random.randint(0,1)
            if monsterwantstoblock == 1:
                print("")