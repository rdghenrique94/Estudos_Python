def main():
    nome = str(input("Digite seu nome: ")).strip().upper()
    print("Seu nome tem {} letras A".format(nome.count('A')))
    print("A primeira letra A apareceu na prosição {}".format(nome.find('A')))
    print("A ultima letra A apareceu na posição {}".format(nome.rfind('A')))


main()