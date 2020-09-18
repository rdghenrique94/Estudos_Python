from aula5exC1 import Infos
def main():
    fila1 = Infos()
    print("Fila Vazia",fila1.ins())
    fila1.getInserir("IESP")
    fila1.getInserir("ED")
    fila1.getInserir("2019.2")
    fila1.getInserir("João Pessoa")
    fila1.getInserir("Estagio 2")
    print("Fila Completa",fila1.ins())

main()