def main():
    pm = float(input("Peso do Animal: "))
    g1 = input("Qual grupo o animal pertence? ")

    if g1 == "1":
        k = 129
        tmb = (pm**0.75)*k
        print("O animal pertence ao grupo dos Passeriformes")
        print("A Taxa Metabolica Basal do animal é de : {:.2f}".format(tmb))

    elif g1 == "2":
        k = 78
        tmb = (pm**0.75)*k
        print("O animal pertence ao grupo dos Não Passeriformes")
        print("A Taxa Metabolica Basal do animal é de : {:.2f}".format(tmb))

    elif g1 == "3":
        k = 70
        tmb = (pm ** 0.75) * k
        print("O animal pertence ao grupo dos Mamíferos Placentários")
        print("A Taxa Metabolica Basal do animal é de : {:.2f}".format(tmb))

    elif g1 == "4":
        k = 49
        tmb = (pm ** 0.75) * k
        print("O animal pertence ao grupo dos Marsupiais e Edentadas")
        print("A Taxa Metabolica Basal do animal é de : {:.2f}".format(tmb))

    elif g1 == "5":
        k = 10
        tmb = (pm ** 0.75) * k
        print("O animal pertence ao grupo dos Repteis")
        print("A Taxa Metabolica Basal do animal é de : {:.2f}".format(tmb))
    else:
        print("Comandos Invalidos")
        print("Tente Novamente")
        return main()





main()