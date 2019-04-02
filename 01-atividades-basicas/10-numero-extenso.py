# Atividade 10
# Proposta =>

# Leia um número inteiro entre 20 e 59 e mostre seu extenso.
# Exiba um erro se o número estiver fora do intervalo.


cont = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
    'vinte', 'vinte e um', 'vinte e dois', 'vinte e três', 'vinte e quatro', 'vinte e cinco', 'vinte e seis',
    'vinte e sete', 'vinte e oito', 'vinte e nove', 'trinta', 'trinta e um', 'trinta e dois',
    'trinta e três', 'trinta e quatro', 'trinta e cinco', 'trinta e seis', 'trinta e sete', 'trinta e oito',
    'trinta e nove', 'quarenta', 'quarenta e um', 'quarenta e dois', 'quarenta e três', 'quarenta e quatro',
    'quarenta e cinco', 'quarenta e seis', 'quarenta e sete', 'quarenta e oito', 'quarenta e nove',
    'cinquenta', 'cinquenta e um', 'cinquenta e dois', 'cinquenta e três', 'cinquenta e quatro',
    'cinquenta e cinco', 'cinquenta e seis', 'cinquenta e sete', 'cinquenta e oito', 'cinquenta e nove'
)

while (True):
    numero = int(input("Informe um número entre 20 e 59: "))
    if (numero < 20 or numero > 59):
        print('\nFavor, insira um número entre 20 e 59\n')
    else:
        break

print(f'Você digitou o número -> {cont[numero]}')
