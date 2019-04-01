# Atividade 02
# Proposta =>

# Leia 4 números inteiros e encontre a média aritmética simples
# entre as que correspondem a números pares. Lembre-se que não
# pode haver divisão por zero.

# Captura o número inserido e armazena nas variáveis.
n1 = input("Informe o 1º Número inteiro: ")
n2 = input("Informe o 2º número inteiro: ")
n3 = input("Informe o 3º número inteiro: ")
n4 = input("Informe o 4º número inteiro: ")

# Faz a soma de todos os números inseridos e armazena em "n"
n = (int(n1) + int(n2) + int(n3) + int(n4))

# Calcular a média aritmética.
media = (n / 4)

print('\nA Média dos números inseridos foi de', media)
