# Atividade 01
# Proposta =>

# Leia um número inteiro e mostra uma mensagem indicando
# se este número é par ou impar, e se é positivo ou negativo.

numero = input("Informe um número inteiro: ")

n = (int(numero) % 2)

# Valida se é ímpar ou par
result = 'O número inserido foi Ímpar!' if n != 0 else 'O número inserido foi Par!'

# Valida se é positivo ou negativo
sinal = ' Número Positivo!' if int(numero) > 0 else ' Número Negativo!'

# Outra forma de fazer

# # Verifica se é Par ou Ímpar
# if (n != 0):
#     result = 'O número inserido foi Ímpar!'
# else:
#     result = 'O número inserido foi Par!'
#
# # Valida se é positivo ou negativo
# if (int(numero) > 0):
#     sinal = ' Número Positivo!'
# else:
#     sinal = ' Número Negativo!'

print(result + sinal)
