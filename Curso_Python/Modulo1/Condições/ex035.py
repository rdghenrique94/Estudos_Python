'''def main():
    a = float(input("Primeira Reta: "))
    b = float(input("Segunda Reta: "))
    c = float(input("Terceira Reta: "))

    if  (b-c) < a and a < (b+c) or (a-b) < c and c < (a+b) or (a-c) < b and b < (a+c) :
        print("As retas formão um triangulo")
    else:
        print("As retas não formam um triangulo")




main()
'''
print("="*30)
print("Analisando Triangulos")
print("="*30)
r1 = float(input("Primeiro Segmento: "))
r2 = float(input("Segundo Segmento: "))
r3 = float(input("Terceiro Segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os Segmentos formão um Triangulo")
else:
    print("Os segmentos não formão um Triangulo")