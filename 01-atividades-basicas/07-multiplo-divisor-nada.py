# Atividade 07
# Proposta =>

# Leia os números inteiros A e B e informe se A é múltiplo,
# divisor ou nada de B.

# Captura os números informados armazena na variável.
A = input("Informe o 1º número: ")
B = input("Informe o 2º número: ")

# Convertendo as idades para inteiro para evitar erros
A = int(A)
B = int(B)

# Verifica se é múltiplo
multiplo = str(A) + " é múltiplo de " + str(B) if A % B == 0 else ''
print(multiplo)

# Verifica se é divisor ou nada.
divisor = str(A) + " é divisor de " + str(B) if B % A == 0 else str(A) + " não é nada de " + str(B)
print(divisor)
