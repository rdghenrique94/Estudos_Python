#EXERCICIO H
import time

def Salario(H,V):
    print("Calculando o Salario Bruto...")
    time.sleep(1)
    Salario = True
    while Salario:
        Salario = (H * V)
        print("O valor Bruto do seu Salario é:       R$%.2f" %Salario)
        time.sleep(2)
        break

def IPRF(H,V):
    print("Calculando o Imposto de Renda...")
    time.sleep(1)
    IPRF = True
    while IPRF:
        IPRF = (((H * V) * 11) / 100)
        print("O valor do imposto debitado é:        R$%.2f" %IPRF)
        time.sleep(2)
        break

def INSS(H,V):
    print("Calculando o INSS...")
    time.sleep(1)
    INSS = True
    while INSS:
        INSS = (((H * V) * 8) / 100)
        print("O valor do imposto INSS é:            R$%.2f" %INSS)
        time.sleep(2)
        break

def Sindicato(H,V):
    print("Calculando a taxa de contribuição Sindical... ")
    time.sleep(1)
    Sindicato = True
    while Sindicato:
        Sindicato = (((H * V) * 5) / 100)
        print("O valor da contribuição Sindical é:   R$%.2f" %Sindicato)
        time.sleep(2)
        break

def SalarioL(H,V):
    print("Calculando salario Liquido...")
    time.sleep(1)
    SalarioL = True
    while SalarioL:
        SalarioL = (H * V) - (((H * V) * 24) / 100)
        print("O valor do salario Liquido é:         R$%.2f" %SalarioL)
        time.sleep(2)
        break

def Desconto(H,V):
    print("Calculando desconto no salario...")
    time.sleep(1)
    Desconto = True
    while Desconto:
        Desconto = (((H * V) * 24) / 100)
        print("O valor dos descontos é de:           R$%.2f" %Desconto)
        time.sleep(2)
        break

def Resumo(H,V):
    print("")
    print("Imprimindo resumo...")
    time.sleep(2)
    Resumo = True
    while Resumo:
        Salario = (H * V)
        IPRF = (((H * V) * 11) / 100)
        INSS = (((H * V) * 8) / 100)
        Sindicato = (((H * V) * 5) / 100)
        SalarioL = (H * V) - (((H * V) * 24) / 100)
        Desconto = (((H * V) * 24) / 100)
        print("O valor Bruto do seu Salario é:       R$%.2f" %Salario)
        print("O valor do imposto debitado é:        R$%.2f" %IPRF)
        print("O valor do imposto INSS é:            R$%.2f" %INSS)
        print("O valor da contribuição Sindical é:   R$%.2f" %Sindicato)
        print("O valor do salario Liquido é:         R$%.2f" %SalarioL)
        print("O valor dos descontos é de:           R$%.2f" %Desconto)
        print("")
        break

def Main():
    Main = True
    while Main:
        H = float(input("Digite o numero de horas trabalhadas: "))
        V = float(input("Digite o valor da hora trabalhada: "))
        print("")

        Salario(H,V)
        IPRF(H,V)
        INSS(H,V)
        Sindicato(H,V)
        SalarioL(H,V)
        Desconto(H,V)
        Resumo(H,V)

        time.sleep(3)
        Main = True

Main()