# Atividade 03
# Proposta =>

# Leia 4 notas, calcule a média dessas e escreva.
# Reprovado (média <5). Recuperação (média <= 5 e <7)
# e Aprovado (média >=7)

# Captura o número inserido e armazena nas variáveis.
n1 = input("Informe a 1º Nota: ")
n2 = input("Informe a 2º Nota: ")
n3 = input("Informe a 3º Nota: ")
n4 = input("Informe a 4º Nota: ")

# Faz a soma de todos as notas e calcul a média
media = ((float(n1) + float(n2) + float(n3) + float(n4)) / 4)

if (media < 5):
    print('\nReprovado, sua média final foi de -> ', media)
elif (media >= 5 and media < 7):
    print('\nRecuperação, sua média final foi de -> ', media)
elif (media > 7):
    print('\nAprovado, sua média final foi de -> ', media)
