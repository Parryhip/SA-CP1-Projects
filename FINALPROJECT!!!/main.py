#Samuel Andelin, FINAL PROJECT!!!
import random
import time
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
    'inventory' : []
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
    'inventory' : []
}