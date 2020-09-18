def main():
    casa = float(input("Qual Valor da Casa: R$ "))
    salario = float(input("Qual o valor do Salario: R$  "))
    anos = int(input("Quantos anos será o financiamento: "))
    prest = casa / (anos*12)
    minimo = salario * 0.30
    print("="*20)
    print("Para pagar uma casa de R$ {:.2f} em {} anos".format(casa, anos))
    print("A prestação será de R$ {:.2f} ".format(prest))
    print("=" * 20)
    print("Comparando tem que pagar {:.2f} e o minimo é {}".format(prest, minimo))


    if prest <= minimo:
        print("Seu Emprestimo foi Concedido")
    else:
        print("Seu Emprestimo foi Negado")




main()