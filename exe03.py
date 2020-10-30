# Exercicio 03

def pn(n):
    if n > 0:
        return 'Positivo'
    elif n == 0:
        return 'Nulo'
    else:
        return 'Negativo'


print('POSITIVO OU NEGATIVO')
n = int(input('digite um número: '))
print(f'Este número é {pn(n)}')

