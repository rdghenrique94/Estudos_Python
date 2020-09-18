def salarioBruto(valorH, horasT):
    return valorH * horasT

def descontoIR(salBrt):
    return salBrt *0.11

def descontoIN(salBrt):
    return salBrt * 0.08

def descontoSind(salBrt):
    return salBrt * 0.05


def main():
    valorHora = float(input('valor da hora: '))
    horasTrabalhadas = float(input('horas trabalhadas: '))

    salBr = salarioBruto(valorHora, horasTrabalhadas)
    print("Salario Bruto",salBr)
    descIR =descontoIR(salBr)
    print("Desconto do Imposto de Renda",descIR)
    descIN = descontoIN(salBr)
    print("Desconto do INSS", descIN)
    descSin = descontoSind(salBr)
    print("Desconto do Sindicato",descSin)





main()
