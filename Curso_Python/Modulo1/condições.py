def main():
    nome = str(input('qual seu nome? '))
    if nome == 'Rodrigo':
        print("que belo nome!")

    else:
        print('que nome feio')
    print("olá {}".format(nome))

    n1 = float(input("Digite a primeira Nota"))
    n2 = float(input("Digite a segunda Nota"))
    m = (n1 + n2) / 2
    #print("PARABENS" if m >= 6 else "ESTUDE MAIS")
    if m >= 6:
        print("Você passou")
    else:
        print("Você está na Final")


main()
