from math import hypot

def main():
    catetoOP = float(input("Digite o valor do Cateto Oposto: "))
    catetoAD = float(input("Digite o valor do Cateto Adjacente: "))
    #hi = hypot(catetoOP, catetoAD)
    print("O comprimento da Hipotenuza é {:.2f}".format(hypot(catetoOP, catetoAD)))
main()