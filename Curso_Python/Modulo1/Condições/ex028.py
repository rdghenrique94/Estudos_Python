from random import randint
def main():
    comp = randint(0, 5)
    print("-"*10)
    print("Vou pensar em um número entre 0 e 5. Tente Adivinhar...")
    print("-" * 10)
    player = int(input("Em que número pensei?  "))

    if player == comp:
        print("Congratulations, you won")
    else:
        print("Ganhei, Eu pensei no numero {} e não no {}".format(comp, player))

main()


'''def main():
    num = int(input("Digite um número entre 0 e 5"))
    if num >= 0 and num <= 5:
        print("You Won")
    else:
        print("You Lose")


main()            
'''
