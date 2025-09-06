import math

def arredondamentos(numero):
    piso = math.floor(numero)
    teto = math.ceil(numero)
    arredondado = round(numero)
    return piso, teto, arredondado

def main():
    n1 = float(input("Digite o primeiro número: "))
    return arredondamentos(n1)

if __name__ == "__main__":
    resultado = main()
    print(resultado)
    