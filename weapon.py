import random
weapon_list = ['knife', 'sword', 'long sword', 'spear']

def gera_weapon():
    weapon_chance = random.randint(1,10)
    if weapon_chance == 1 or weapon_chance == 3:
        weapon_choice = random.randint(0,len(weapon_list))
        return weapon_list[weapon_choice]
    return None








