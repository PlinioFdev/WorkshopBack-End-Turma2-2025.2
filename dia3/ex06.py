#dados = {
 #   "nome": "Isaac ",
  #  "idade": 25,
   # "cidade": "São Paulo"
#}

#chave = input("Digite a chave que deseja acessar: ")

#print(f"O valor da chave '{chave}' é: {dados[chave]}")


#codigo corrigido:
dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}
try:
    chave = input("Digite a chave que deseja acessar: ")

    print(f"O valor da chave '{chave}' é: {dados[chave]}")
except KeyError:
    print("Desculpe, essa chave não existe no dicionário! ): ")
except KeyboardInterrupt:
    print("\nEntrada interrompida pelo usuário.")
except EOFError:
    print("\nEntrada finalizada inesperadamente.")
except Exception as e: 
    print(f"Ocorreu um erro inesperado: {e}")
    