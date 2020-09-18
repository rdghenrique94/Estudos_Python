def main():
    nota1 = float(input("Digite a primeira nota do Aluno: "))
    nota2 = float(input("Digite a segunda nota do Aluno: "))

    med = (nota1+nota2)/2

    if med < 5.0:
        print("O Aluno está REPROVADO")
    elif med == 5.0 and med <= 6.9:
        print("O Aluno está em RECUPERAÇÃO")
    elif med >= 7.0:
        print("o Aluno está APROVADO")

main()