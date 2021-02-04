import random
from skill import gera_skill
from weapon import gera_weapon
def create_enemy():
    try:
        arquivo_nomes = open('nomes.txt','r')
        arquivo_base = open('char.txt', 'r')

        eName = arquivo_nomes.readlines()
        base = arquivo_base.readlines()

        for x in range(0,len(eName)):
            eName[x] = eName[x].strip('\n')

        for y in range(0, len(base)):
            base[y] = base[y].strip('\n')

        enemy_name = eName[random.randint(0, len(eName))]

        min_sts_str = int(int(base[3]) / 2)
        min_sts_agi = int(int(base[4]) / 2)
        min_sts_spd = int(int(base[5]) / 2)
        min_sts_vit = int(int(base[6]) / 2)

        max_sts_str = int(int(base[3]) + 10)
        max_sts_agi = int(int(base[4]) + 10)
        max_sts_spd = int(int(base[5]) + 10)
        max_sts_vit = int(int(base[6]) + 10)

        Ests_str = random.randint(min_sts_str, max_sts_str)
        Ests_agi = random.randint(min_sts_agi, max_sts_agi)
        Ests_spd = random.randint(min_sts_spd, max_sts_spd)
        Ests_vit = random.randint(min_sts_vit, max_sts_vit)

        Eskill_list = []
        Eweapon_list = []

        sort_skill = gera_skill()
        if sort_skill != None:
            Eskill_list.append(sort_skill)

        sort_weapon = gera_weapon()
        if sort_weapon != None:
            Eweapon_list.append(sort_weapon)


        arquivo_enemy = open('enemy.txt', 'w')

        personagem = list()
        personagem.append(str(enemy_name) + "\n")
        personagem.append(str(Eskill_list) + "\n")
        personagem.append(str(Eweapon_list) + "\n")
        personagem.append(str(Ests_str) + "\n")
        personagem.append(str(Ests_agi) + "\n")
        personagem.append(str(Ests_spd) + "\n")
        personagem.append(str(Ests_vit))

        arquivo_enemy.writelines(personagem)

        arquivo_base.close()
        arquivo_enemy.close()
        arquivo_nomes.close()
    except:
        print("Ocorreu um erro no carregamento do inimigo encaminhe essa mensagem para o suporte")