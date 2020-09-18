from random import choice
import random
def main():
    a1 = input("Primeiro Aluno: ")
    a2 = input("Segundo Aluno: ")
    a3 = input("Terceiro Aluno: ")
    a4 = input("Quarto Aluno: ")
    #names = "Rodrigo", "Danilo", "Renato", "Carlos"
    alunos = [a1, a2, a3, a4]
    escolhido = choice (alunos)
    print("Dos Alunos {}, o escolhido para agapar o quadro será {}".format(alunos, escolhido))




main()

