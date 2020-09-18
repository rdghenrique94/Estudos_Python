import math
def main():
    n = float(input("Digite um numero: "))
    print("A porção inteida do numero {} é {}".format(n, math.trunc(n)))
main()