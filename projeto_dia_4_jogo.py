import random

x = int(input('Escolha entre 0 (Pedra), 1(Papel), 2(Tesoura): '))

pedra = ''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) 
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
if x == 0:
    print(pedra)
    aleatorio = random.randint(0,2)
    if aleatorio == 0:
        print(pedra)
        print('Empate')
    elif aleatorio == 1:
        print(papel)
        print('Computador ganho. GAME OVER')
    else:
        print(tesoura)
        print('Parabens!!! Você ganhou')
elif x == 1:
    print(papel)
    aleatorio = random.randint(0,2)
    if aleatorio == 0:
        print(pedra)
        print('Parabens!!! Você ganhou')
    elif aleatorio == 1:
        print(papel)
        print('Empate')
    else:
        print(tesoura)
        print('Computador ganhou. GAME OVER')
else:
    print(tesoura)
    aleatorio = random.randint(0,2)
    if aleatorio == 0:
        print(pedra)
        print('Computador ganhou. GAME OVER')
    elif aleatorio == 1:
        print(papel)
        print('Parabens!!! Você ganhou')
    else:
        print(tesoura)
        print('Empate')

