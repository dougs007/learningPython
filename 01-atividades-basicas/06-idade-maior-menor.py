# Atividade 06
# Proposta =>

# Leia o nome e a idade de três pessoas e informe o nome da pessoa mais velha
# e o nome da pessoa mais nova. Considere que não existem idades iguais.

# Captura os números informados armazena na variável.
p1 = input("Informe o nome da 1º pessoa: ")
n1 = input("Informe a idade da 1º pessoa: ")
p2 = input("Informe o nome da 2º pessoa: ")
n2 = input("Informe a idade da 2º pessoa: ")
p3 = input("Informe o nome da 3º pessoa: ")
n3 = input("Informe a idade da 3º pessoa: ")

# Convertendo as idades para inteiro para evitar erros
idade1 = int(n1)
idade2 = int(n2)
idade3 = int(n3)

# Faz as validações para saber qual foi o tipo de Operação
if (idade1 > idade2 and idade2 > idade3):
    # Recebe o nome da 1º Pessoa
    maior = p1
    # Recebe o nome da 3º Pessoa
    menor = p3
elif (idade1 > idade3 and idade3 > idade2):
    # Recebe o nome da 1º Pessoa
    maior = p1
    # Recebe o nome da 2º Pessoa
    menor = p2
elif (idade2 > idade1 and idade1 > idade3):
    # Recebe o nome da 2º Pessoa
    maior = p2
    # Recebe o nome da 3º Pessoa
    menor = p3
elif (idade2 > idade3 and idade3 > idade1):
    # Recebe o nome da 2º Pessoa
    maior = p2
    # Recebe o nome da 1º Pessoa
    menor = p1
elif (idade3 > idade1 and idade1 > idade2):
    # Recebe o nome da 3º Pessoa
    maior = p3
    # Recebe o nome da 2º Pessoa
    menor = p2
elif (idade3 > idade2 and idade2 > idade1):
    # Recebe o nome da 3º Pessoa
    maior = p3
    # Recebe o nome da 1º Pessoa
    menor = p1

if (idade1 != idade2 and idade1 != idade3 and idade3 != idade1):
    print('\nA pessoa mais nova é a ->', menor)
    print('A pessoa mais velha é a ->', maior + '')
