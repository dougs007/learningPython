# Atividade 05
# Proposta =>

# Leia dois números inteiros, uma operação matemática (+,-,*,/)
# e faça o cálculo destes números segundo a operação lida

# Captura os números informados armazena na variável.
n1 = input("Informe o 1º número: ")
n2 = input("Informe o 2º número: ")

# Captura a operação informada e armazena na variável.
operacao = input("Informe a operação: ")

# Faz as validações para as Operações.
if operacao != '*' and operacao != '+' and operacao != '-' and operacao != '/':
    print('\nOperação Inválida')
else:

    # Faz as validações para saber qual foi o tipo de Operação
    if (operacao == '*'):
        resultado = (int(n1) * int(n2))
    elif (operacao == '+'):
        resultado = (int(n1) + int(n2))
    elif (operacao == '-'):
        resultado = (int(n1) - int(n2))
    elif (operacao == '/'):
        resultado = (int(n1) / int(n2))

print('O resultado foi de ->', resultado)
