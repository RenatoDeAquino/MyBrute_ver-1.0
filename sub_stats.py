import random
#esquica com base na agi e o máximo de esquiva é 40% dos golpes
#entre 10 e 19 é 10% entre 20 e 29 é 20% e assim por diante
def esquiva(sts_agi):
    
    chance = random.randint(1,10)
    
    if sts_agi >= 10 and sts_agi < 20:
        if chance == 1:
            return True
        else:
            return False
    elif sts_agi >= 20 and sts_agi < 30:
        if chance == 1 or chance == 2:
            return True
        else:
            return False
    elif sts_agi >= 30 and sts_agi < 40:
        if chance == 1 or chance == 2 or chance == 3:
            return True
        else:
            return False
    elif sts_agi >= 40:
        if chance == 1 or chance == 2 or chance == 3 or chance == 4:
            return True
        else:
            return False

def damage(sts_str):
    return (sts_str / 2) * 0.5

def double_atack(sts_spd):
    chance = random.randint(1,10)
    
    if sts_spd >= 10 and sts_spd < 20:
        if chance == 1:
            return True
        else:
            return False
    elif sts_spd >= 20 and sts_spd < 30:
        if chance == 1 or chance == 2:
            return True
        else:
            return False
    elif sts_spd >= 30 and sts_spd < 40:
        if chance == 1 or chance == 2 or chance == 3:
            return True
        else:
            return False
def conter_atack(sts_spd):
    chance = random.randint(1,10)
    
    if sts_spd >= 10 and sts_spd < 20:
        if chance == 1:
            return True
        else:
            return False
    elif sts_spd >= 20 and sts_spd < 30:
        if chance == 1 or chance == 2:
            return True
        else:
            return False
    elif sts_spd >= 30 and sts_spd < 40:
        if chance == 1 or chance == 2 or chance == 3:
            return True
        else:
            return False






