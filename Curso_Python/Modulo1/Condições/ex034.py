def main():
    sal = float(input("Digite seu salario: "))

    if sal <= 1250:
        sal1 = sal * 0.15
        newsal = sal+sal1
        print("Seu salario de {:.2f} R$ teve um aumento de {:.2f} R$, ficando {:.2f} R$".format(sal, sal1, newsal))
    elif sal > 1250:
        sal2 = sal * 0.10
        newsal = sal+sal2
        print("Seu salario de {:.2f} R$, teve um aumento de {:.2f} R$, ficando {:.2f} R$". format(sal, sal2, newsal))

main()