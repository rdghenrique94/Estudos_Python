def main():

    peso = float(input("Digite seu Peso: "))
    altu = float(input("Digite sua Altura: "))

    imc = peso / (altu**2)

    if imc < 18.5:
        print("Você está Abaixo do peso")
        print("Taxa de IMC {:.2f}".format(imc))
    elif 18.5 <= imc < 25:
        print("Você está no peso Ideal")
        print("Taxa de IMC {:.2f}".format(imc))
    elif 25 <= imc < 30:
        print("Você está acima do peso")
        print("Grau: Sobrepeso")
        print("Taxa de IMC {:.2f}".format(imc))
    elif 30 <= imc < 40:
        print("Você está acima do peso")
        print("Grau: Obesidade")
        print("Taxa de IMC {:.2f}".format(imc))
    elif imc >= 40:
        print("Você está muito acima do peso")
        print("Grau: Obesidade Mórbida")
        print("Taxa de IMC {:.2f}".format(imc))
    else:
        print("Digite suas informações novamente")
main()