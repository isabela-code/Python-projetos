import random

print("Bem vindo ao gerador de senhas")
x = int(input('Quantas letras você vai querer: '))
y = int(input('Quantos simbolos você vai querer: '))
z = int(input('Quantos numeros você vai querer: '))
senha = []
soma = x+y+z
final = []

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p' , 'q', 'r', 's' , 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P' , 'Q', 'R', 'S' , 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '=', '+']

for i in range(0,x):
    senha += random.choices(letras)
for i in range(0,y):
    senha += random.choices(simbolos)
for i in range(0,z):
    senha+= random.choices(numeros)
final += random.sample(senha,soma)
lista = ''
for i in final:
    lista += i
print(lista)
    