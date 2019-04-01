# Atividade 04
# Proposta =>

# Leia a idade de um nadador e exiba sua categoria segundo as regras:
# A (5 até 7), B (8 até 10), C (11 até 13), D (14 até 18)
# E (idade > 18)

# Captura a idade inserido e armazena na variável.
idade = int(input("Informe sua idade: "))

# Faz as validações para definir a Categoria
if idade > 0 and idade <= 7:
    print('\nSua categoria é a A')
elif idade >= 8 and idade <= 10:
    print('\nSua categoria é a B')
elif idade >= 11 and idade <= 13:
    print('\nSua categoria é a C')
elif idade >= 14 and idade <= 18:
    print('\nSua categoria é a D')
elif idade > 18:
    print('\nSua categoria é a E')
# Caso o valor informado seja menor que 0 ou seja número negativo.
else:
    print('\nIdade inválida')
