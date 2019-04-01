# Atividade 08
# Proposta =>

# Leia três números e mostre-os em ordem crescente

# Captura os números informados armazena na variável.
n1 = input("Informe o 1º número: ")
n2 = input("Informe o 2º número: ")
n3 = input("Informe o 3º número: ")

# Verifica e Ordena
if (n1 > n2 and n2 > n3):
    print('Ordem ->', n3 + ' ' + n2 + ' ' + n1)

elif (n1 > n3 and n3 > n2):
    print('Ordem ->', n2 + ' ' + n3 + ' ' + n1)

elif (n2 > n1 and n1 > n3):
    print('Ordem ->', n3 + ' ' + n1 + ' ' + n2)

elif (n2 > n3 and n3 > n1):
    print('Ordem ->', n1 + ' ' + n3 + ' ' + n2)

elif (n3 > n1 and n1 > n2):
    print('Ordem ->', n2 + ' ' + n1 + ' ' + n3)

elif (n3 > n2 and n2 > n1):
    print('Ordem ->', n1 + ' ' + n2 + ' ' + n3)
