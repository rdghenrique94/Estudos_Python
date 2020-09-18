def main():

    print("="*30)
    print("Analisando Triangulos")
    print("="*30)

    r1 = float(input("Primeiro Segmento: "))
    r2 = float(input("Segundo Segmento: "))
    r3 = float(input("Terceiro Segmento: "))

    if r1 == r2 != r3 or r1 == r3 != r2 or r2 == r1 != r3 or r2 == r3 != r1 or r3 == r1 != r2 or r3 == r2 != r1:
        print("O triangulo é Isorceles")

    elif r1 == r2 == r3:
        print("O triangulo é Equilatero")
    elif r1 != (r2 != r3) or r1 != (r3 != r2) or r2 != (r1 != r3) or r2 != (r3 != r2) or r3 != (r1!=r2) or r3 !=(r2!=r1):
        print("O triangulo é Escaleno")
    return main()

main()