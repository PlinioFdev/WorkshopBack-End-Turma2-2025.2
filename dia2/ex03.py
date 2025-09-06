import math

class CalculadoraGeometrica:
    @staticmethod
    def area_circulo(raio):
        return math.pi * math.pow(raio, 2)

    @staticmethod
    def area_triangulo(base, altura):
        return (base * altura) / 2

    @staticmethod
    def hipotenusa(cateto1, cateto2):
        return math.sqrt(math.pow(cateto1, 2) + math.pow(cateto2, 2))

def menu():
    opcoes = {
        "1": "Área do círculo",
        "2": "Área do triângulo",
        "3": "Hipotenusa do triângulo retângulo"
    }
    return opcoes

def executar_calculo(escolha, valores):
    if escolha == "1":
        return CalculadoraGeometrica.area_circulo(valores[0])
    elif escolha == "2":
        return CalculadoraGeometrica.area_triangulo(valores[0], valores[1])
    elif escolha == "3":
        return CalculadoraGeometrica.hipotenusa(valores[0], valores[1])
    else:
        return None

def main():
    opcoes = menu()
    escolha = input("Digite o número da opção (1-Área do círculo, 2-Área do triângulo, 3-Hipotenusa): ")
    valores = []
    if escolha == "1":
        raio = float(input("Digite o raio do círculo: "))
        valores = [raio]
    elif escolha == "2":
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        valores = [base, altura]
    elif escolha == "3":
        cateto1 = float(input("Digite o valor do primeiro cateto: "))
        cateto2 = float(input("Digite o valor do segundo cateto: "))
        valores = [cateto1, cateto2]
    else:
        return "Opção inválida."
    resultado = executar_calculo(escolha, valores)
    return resultado

if __name__ == "__main__":
    resultado = main()
    print(resultado)
