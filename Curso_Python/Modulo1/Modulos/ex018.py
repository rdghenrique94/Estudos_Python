from math import radians, sin, cos, tan
def main():
    ang = float(input("Digite o valor de um Angulo qualquer: "))
    seno = sin(radians(ang))
    coss = cos(radians(ang))
    tang = tan(radians(ang))
    print("O Ângulo {}, tem como seno {:.2f}, cosseno {:.2f} e tangente {:.2f}". format(ang, seno, coss, tang))
main()