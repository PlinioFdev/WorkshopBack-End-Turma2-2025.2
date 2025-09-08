#def dividir(a, b):
#    return a / b

#num1 = input("Digite o primeiro número: ")
#num2 = input("Digite o segundo número: ")

#resultado = dividir(int(num1), int(num2))
#print(f"Resultado: {resultado}")







#codigo corrigido:
def dividir(a, b):
    return a / b
try:
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")

    resultado = dividir(int(num1), int(num2))
    print(f"Resultado: {resultado}")
except ValueError:
    print("Você não digitou um número valido!")  #erro caso o usuario digite um numero invalido ou str
except ZeroDivisionError:
    print("A divisão não pode ser feita por 0")  #erro caso o usuario digite 0
