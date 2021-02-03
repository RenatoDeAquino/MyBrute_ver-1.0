import os
def load_char():
    try:
        arquivo = open("char.txt",'r')

        char = arquivo.readlines()

        for x in range(0,len(char)):
            char[x] = char[x].strip('\n')

        print("Seja bem vindo novamente " + char[0])

        arquivo.close()

    except:
        print("voce não possui um arquivo de persoagem isso você não possui um personagem salvo")
        print("ou o arquivo do seu personagem foi deletado")


    
load_char()
