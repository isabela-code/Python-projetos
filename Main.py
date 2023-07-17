from Cafeteria_poo import Cafe

print('Bem vindo a cafeteria Zobinha Queiroz')
vezes = int(input('Quantas bebidas você vai querer: '))

cafe = Cafe()

while vezes > 0:
    print('O que você gostaria? (expresso/latte/cappuccino)')
    escolha = input()
    cafe.fazer_cafe(escolha)
    vezes -= 1
print('Obrigado por comprar na cafeteria Zobinha Queiroz')
print()
cafe.relatorio()
print('Os pedidos acabaram, deseja desligar a maquina?')
x = input()
if x == 'sim':
    print('Digite o codigo de desligamento')
    y = input()
    if y == '1234':
        cafe.desligar(codigo=True)
    else:
        print('Você não tem o codigo de desligamento, portanto não foi possivel desligar a maquina')
        cafe.desligar(codigo=False)
else:
    cafe.desligar(codigo=False)