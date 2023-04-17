lista1 = ['', '', '']
lista2 = ['', '', '']
lista3 = ['', '', '']
mapa = [lista1, lista2, lista3]
print(f'{lista1}\n{lista2}\n{lista3}\n')
x = input('Qual posição você quer colocar o seu tesouro: ')

horizontal = int(x[0])
vertical = int(x[1])

parte = mapa[vertical - 1]
parte[horizontal - 1] = 'X'

print(f'{lista1}\n{lista2}\n{lista3}\n')