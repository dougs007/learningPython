# Atividade 09
# Proposta =>

# Leia uma milhar e informe se esse número é Palíndromo.
# Exemplos de números palíndromos: 9889, 7337, 2002

# Captura os números informados armazena na variável.
numero = input("Informe um milhar : ")

# Inverte o valor do número recebido.
palindromo = reversed(numero)
palindromo = ''.join(reversed(numero))

# Verifica se o número é igual a ele mesmo no inverso.
if (numero == palindromo):
    print('{} É um Palíndromo de {}'.format(numero, palindromo))
else:
    print('{} Não é um Palíndromo de {}'.format(numero, palindromo))
