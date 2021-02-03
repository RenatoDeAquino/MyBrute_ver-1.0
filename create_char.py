import random
from skill import gera_skill
from weapon import gera_weapon
def create_char():
    #minimo e maximo status para criação de personagem
    min_sts = 10
    max_sts = 20
    #lista de habilidades do personagem
    skill_list = []
    #lista de armas do personagem
    weapon_list = []
    #pegando o nome do personagem
    user_input = input("\nDigite o nome do seu personagem\n->")
    #status base do personagem
    sts_str = random.randint(min_sts,max_sts)
    sts_agi = random.randint(min_sts,max_sts)
    sts_spd = random.randint(min_sts,max_sts)
    sts_vit = random.randint(min_sts,max_sts)
    #chamamento para geração da possibilidade de se ter habilidade e qual é
    sort_skill = gera_skill()
    if sort_skill != None:
        skill_list.append(sort_skill)
    #-----------------------------------------------------------------------
    #chamamento para a geração da possibilidade de se ter uma arma e qual é
    sort_weapon = gera_weapon()
    if sort_weapon != None:
        weapon_list.append(sort_weapon)
    #-----------------------------------------------------------------------
    #apenas para debugar
    # print("Seu personagem de nome " + str(user_input) + " possui os seguintes stats")
    # print("Habilidades: " + str(skill_list))
    # print("Armas: " + str(weapon_list))
    # print("FORÇA -> " + str(sts_str))
    # print("AGILIDADE -> " + str(sts_agi))
    # print("VELOCIDADE -> " + str(sts_spd))
    # print("VITALIDADE -> " + str(sts_vit))

    arquivo = open("char.txt", "w")
    
    personagem = list()
    personagem.append(str(user_input) + "\n")
    personagem.append(str(skill_list) + "\n")
    personagem.append(str(weapon_list) + "\n")
    personagem.append(str(sts_str) + "\n")
    personagem.append(str(sts_agi) + "\n")
    personagem.append(str(sts_spd) + "\n")
    personagem.append(str(sts_vit) + "\n")

    arquivo.writelines(personagem)

    arquivo.close()






