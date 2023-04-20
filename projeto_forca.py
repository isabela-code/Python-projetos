import random 

forca = '''
         _______
        |       |
        |       
        |
        |
        |
        |
    ¨¨¨¨¨¨¨¨¨¨
    '''
cabeça = '''
         _______
        |       |
        |       Ô
        |
        |
        |
        |
    ¨¨¨¨¨¨¨¨¨¨
    '''
tronco = '''
         _______
        |       |
        |       Ô
        |       |
        |       |
        |      
        |
    ¨¨¨¨¨¨¨¨¨¨
    '''
perna1 = '''
         _______
        |       |
        |       Ô
        |       |
        |       |
        |      /
        |
    ¨¨¨¨¨¨¨¨¨¨
    '''
perna2 = '''
         _______
        |       |
        |       Ô
        |       |
        |       |
        |      / \
        |
    ¨¨¨¨¨¨¨¨¨¨
    '''
braço1 = '''
         _______
        |       |
        |       Ô
        |      \|
        |       |
        |      / \
        |
    ¨¨¨¨¨¨¨¨¨¨
    '''
braço2 = '''
         _______
        |       |
        |       Ô
        |      \|/
        |       |
        |      / \  
        |
    ¨¨¨¨¨¨¨¨¨¨
    '''
palavras = ['banana', 'estojo', 'chuveiro', 'banheiro','cama', 'brasil', 'computador']
escolha = random.choice(palavras)
x = input("Escolha uma letra: ").lower()
linha = []
final = []

for i in escolha:
    linha += '_'
tamanho = len(linha)
print(f'Sua palavra tem {tamanho} letras')
z = -1
passa = tamanho * tamanho
soma = 0 
chance = 6

for i in escolha:
    final += i

while final != linha and chance != 0:
    for i in escolha:
        z+=1
        for posi in linha:
            if i == x:
                posi = x
                linha[z] = posi
    for i in escolha:
        for s in linha:
            if x != i:
                soma += 1
                if soma == passa:
                    chance -= 1
            else:
                soma += 0
    soma = 0 
    z = -1
    if chance == 6:
        print(forca)
    elif chance == 5:
        print(cabeça)
    elif chance == 4:
        print(tronco)
    elif chance == 3:
        print(perna1)
    elif chance == 2:
        print(perna2)
    elif chance == 1:
        print(braço1)
    else:
        print(braço2)
    if final != linha and chance >= 1:
        print(f'Você tem mais {chance} chances')
        print(linha)
        x = input('Escolha outra letra: ')
    if final != linha and chance == 0:
        print('Você perdeu :(')
        print(f'Sua palavra era {escolha}')
    elif final == linha and chance >= 1:
        print('Parabens, você adivinhou a palavra')
        print(linha)