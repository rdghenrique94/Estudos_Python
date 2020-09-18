from random import randint

itens = ("pedra", "papel", "tesoura")
comp = randint(0, 2)
print("""Escolha sua opção 
[0] Pedra
[1] Papel
[2] Tesoura""")
user = int(input("Qual sua joagada? "))
print("="*12)
print("Computador jogou {}".format(itens[comp]))
print("Jogador jogou {}".format(itens[user]))
print("="*12)

if comp == 0:
    if user == 0:
        print("EMPATE")
    elif user == 1:
        print("JOGADOR VENCE")
    elif user == 2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVALIDA")

elif comp == 1:
    if user == 0:
        print("EMPATE")
    elif user == 1:
        print("JOGADOR VENCE")
    elif user == 2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVALIDA")

elif comp == 2:
    if user == 0:
        print("EMPATE")
    elif user == 1:
        print("JOGADOR VENCE")
    elif user == 2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVALIDA")
