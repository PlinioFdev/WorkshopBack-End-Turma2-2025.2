import math

def calcular_raiz_quadrada(numero):
    raiz = math.sqrt(numero)
    return f"A raiz quadrada de {numero} é {raiz:.2f} !"

def main():
    n1 = int(input("Digite o primeiro número: "))
    resultado = calcular_raiz_quadrada(n1)
    return resultado

if __name__ == "__main__":
    print(main())
