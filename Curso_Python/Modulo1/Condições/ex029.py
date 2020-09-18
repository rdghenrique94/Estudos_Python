def main():
    vel = float(input("Digite a Velocidade do Carro: "))

    if vel > 80:
        multa = (vel - 80) * 7
        print("Você foi mulatdo a {} km, e vai ter que pagar {:.2f} R$ de multa".format(vel, multa))
    elif vel <= 20:
        multa1 = (vel + 20) * 7
        print("Você foi multado em {} R$ por andar muito devagar".format(multa1))
    else:
        print("Você não foi Multado")

main()
