def main():
    price = float(input("Qual o preço do produto: R$  "))
    print("""Formas de Pagamento
    [1] á vista dinheiro/cheque
    [2] á vista no cartão
    [3] 2x no cartão
    [4] 3x ou mais no cartão""")
    opc = int(input("Escolha sua opção de pagamento"))

    if opc == 1:
        total = price - (price*.010)
        print("Sua compra de R$ {:.2f} vai custar R$ {:.2f}".format(price, total))
    elif opc == 2:
        total = price - (price * 0.05)
        print("Sua compra de R$ {:.2f} vai custar R$ {:.2f}".format(price, total))
    elif opc == 3:
        total = price - (price / 2)
        print("Sua compra será parcelada em 2x de R$ {}".format(total))
    elif opc == 4:
        total = price + (price * 0.20)
        totalparc = int(input("Quantas Parcelas? "))
        parc = total / totalparc
        print("Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS". format(totalparc, parc))
        print("sua compra de R$ {:.2f} vai custar R$ {:.2f} no final".format(price, total))


main()