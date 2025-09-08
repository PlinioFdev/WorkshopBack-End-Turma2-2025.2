#numeros = [10, 20, 30]
#indice = int(input("Digite um índice para acessar a lista: ")) 

#print(numeros[indice])

#Codigo corrigido:

numeros = [10, 20, 30]

try:
    indice = int(input("Digite um índice para acessar a lista: "))
    print(numeros[indice])
except ValueError:
    print("Erro: você não digitou um número válido.")
except IndexError:
    print("Erro: índice fora do intervalo da lista.")

