def country():
    paises = []
    print("Quantos países deseja adicionar?")
    numPaises = int(input("> "))

    for i in range(numPaises):
        entrada = str(input(f"Digite o nome do {i+1}° país: "))
        paises.append(entrada)
    
    print("Os países adicionados foram:")

    for i in range(len(paises)):
        print(paises[i])
    
    print()


def city():
    cidades = []
    resposta = 's'
    cont = 0

    while resposta in 'Ss':
        entrada = str(input("Adicione uma cidade: "))
        cidades.append(entrada)
        print("Deseja adicionar mais uma cidade?\n[S] Sim\n[N] Não")
        resposta = str(input("> "))

    print("As cidades adicionadas foram: ")

    while cont < len(cidades):
        print(cidades[cont])
        cont += 1


def main():
    country()
    city()


main()
