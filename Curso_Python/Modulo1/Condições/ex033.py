def main():
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite um numero: "))
    num3 = int(input("Digite um numero: "))

    if num1 > num2 and num1 > num3:
        print("O número {} é o maior".format(num1))
    elif num2 > num1 and num2 > num3:
        print("O número {} é o maior".format(num2))
    elif num3 > num1 and num3 > num2:
        print("O número {} é o maior".format(num3))
    if num1 < num2 and num1 < num3:
        print("O número {} é o menor".format(num1))
    elif num2 < num1 and num2 < num3:
        print("O número {} é o menor".format(num2))
    elif num3 < num1 and num3 < num2:
        print("O número {} é o menor".format(num3))
    if num1 == num2 or num1 == num3 and num2 == num1 or num2 == num3 and num3 == num1 or num3 == num2:
        print("Os outros Numeros são Iguais")

main()