# Dada uma sequência de números inteiros, imprimir seus quadrados.
# sequência : 0, 1, 4, 9, 16

def main():
        start = int(input("Número de Inicio: "))
        end = int(input("Número de Fim: "))

       # for i in range(start, end +1):
        #    print(i**2)
        i = start
        while (i<=end):
            print(i**2)
            i = i+1
main()
'''
def Numero(n):
    Numero = True
    while Numero:
        for n in range(0,5):
            num = n ** 2
            if num == 0:
                print("Seu quadrado é: ", num)
            if num == 1:
                print("Seu quadrado é: ", num)
            if num == 4:
                print("Seu quadrado é: ", num)
            if num == 9:
                print("Seu quadrado é: ", num)
            if num >= 16:
                print("Seu quadrado é: ", num)
                Numero = False
def Main():
    Main = True
    while Main:
        for num in range(0,5):
            num = int(input("Digite um numero inteiro: "))
        Numero(num)
Main()
'''