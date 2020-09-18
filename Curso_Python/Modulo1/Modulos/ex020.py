#import random
from random import shuffle
def main():
    n1 = str(input("Primeiro Aluno: "))
    n2 = str(input("Segundo Aluno: "))
    n3 = str(input("Terceiro Aluno: "))
    n4 = str(input("Quarto Aluno:"))

    #names = ("rodrigo", "danilo", "renato", "carlos")
    lista = [n1, n2, n3, n4]
    #random.shuffle(lista)
    shuffle(lista)
    print("A ordem de apresentação será")
    print(lista)


main()