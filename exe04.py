# Exercicio 04

def soma_imposto(taxa_imposto, custo):
    return (1 + taxa_imposto / 100) * custo


t = float(input('Digite a taxa de imposto: '))
c = float(input('Digite o custo: '))

print('Valor com imposto:', soma_imposto(t, c))
