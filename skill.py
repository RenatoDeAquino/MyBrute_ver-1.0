import random
skill_list = ['+str', '+agi', '+spd', '+vit']

def gera_skill():
    skill_chance = random.randint(1,10)
    if skill_chance == 1 or skill_chance == 2:
        skill_choice = random.randint(0,len(skill_list))
        return skill_list[skill_choice]
    return None








