def main():
    km = int(input("Qual a distancia da sua viagem?: "))

    if km <= 200 and km >= 0:
        km1 = km*0.50
        print("O preço da passagem será {} R$".format(km1))
    else:
        km2 = km*0.45
        print("Sua viagem custara {} R$". format(km2))

main()