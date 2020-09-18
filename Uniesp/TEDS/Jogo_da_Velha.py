#Rodrigo Henrique Soares de Oliveira Andrade

import time

print('''====================================
BEM VINDO AO CLASSICO JOGO DA VELHA
====================================''')
print('''\33[0;30;41mINSTRUÇÕES -> DIGITAR O NUMERO DA LINHA E COLUNA ENTRE 1 E 3
PARA MARCAR SUA POSIÇÃO NO TABULEIRO
CASO UM CAMPO JA ESTEJA PREENCHIDO E O PLAYER JOGAR NELE, O PLAYER PERDERA SUA JOGADA \033[m\n''')

def menu():
    inicio = int(input('Digite 1 para INICIAR ou 0 para SAIR \n'))

    if(inicio == 1):
        for i in [3, 2, 1]:
            print("Iniciando jogo em %s"  % i, end="\n")
            time.sleep(1)
        jogo()

    elif (inicio == 0):
        for i in [3, 2, 1]:
            print("Saindo em %s"  % i, end="\n")
            time.sleep(1)
        exit()

def jogo():
    player = 0

    while velha() == 0:
        print("\n\33[0;30;41mPlayer {} \033[m ".format(player % 2 + 1))
        jogovelha()

        linha = int(input('''\nDigite qual linha será sua Jogada
>1
>2
>3 
='''))

        coluna = int(input('''Qual Coluna será sua Jogada
V   V   V
1   2   3 ='''))
        if linha >3 or linha < 0 or coluna >3 or coluna < 0:
            print("\33[0;30;41mVALORES INVALIDOS, DIGITE VALORES ENTRE 1 E 3\033[m")
            jogo()
        if matriz[linha - 1][coluna - 1] == 0:
            if (player % 2 + 1) == 1:
                matriz[linha - 1][coluna - 1] = 1
            else:
                matriz[linha - 1][coluna - 1] = -1
        else:
            print('''\033[0;30;41mESTE ESPAÇO JÁ ESTÁ PREENCHIDO 
     VOCÊ PERDEU SUA JOGADA\033[m''')
        if velha():
            print("\33[0;30;41mPlayer {} Venceu!\033[m".format(player % 2 + 1))
            jogovelha()
        player += 1

def velha():

    for i in range(3):
        lin = matriz[i][0] + matriz[i][1] + matriz[i][2]
        col = matriz[0][i] + matriz[1][i] + matriz[2][i]
        diagE = matriz[0][0] + matriz[1][1] + matriz[2][2]
        diagD = matriz[2][0] + matriz[1][1] + matriz[2][0]
        if lin == 3 or lin == -3 or col == 3 or col == -3 or diagE == 3 or diagE == -3 or diagD == 3 or diagD == -3:
            return 1
        return 0


def jogovelha():
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == 0:
                print(" * ", end=' ')
            elif matriz[i][j] == 1:
                print(" X ", end=' ')
            elif matriz[i][j] == -1:
                print(" O ", end=' ')
        print()

matriz = [[0 for i in range(3)] for j in range(3)]

def main():
    menu()
main()