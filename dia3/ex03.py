#def somar(a, b):
 #   return a + b

#resultado = somar(10, "5")
#print(resultado)


#O codigo esta errado pois o "5" esta entre aspas, transformando ele em str

#codigo corrigido:

def somar(a, b):
    try:
        return int(a) + int(b)   # tenta converter para inteiro
    except ValueError:
        try:
            return float(a) + float(b)  # tenta como float
        except ValueError:
            return str(a) + str(b)  # se não der, faz concatenação de strings

resultado = somar(10, "5")
print(resultado)  # saída: 15