print("Bem vindo a ilha misteriosa!!!!")
print()
print("SUA MISSÃO É ENCONTRAR O TESOURO")
x = input('Você deseja ir para a direita ou esquerda: \n')
print()
if x == 'esquerda':
    print('Você chegou a um lago, mas não há como passar por ele ser um barco.')
    x = input('Você quer tentar passar pelo lago nadando ou esperar por um barco? \n')
    if x == 'esperar':
        print('Você achou duas portas, uma azul, uma vermelha e uma amarela, escolha com sabedoria!!!!')
        x = input('Qual cor você ira escolher: \n')
        if x == 'azul':
            print('Você foi comido pelos lobos, seu destino foi tragico')
            print('GAME OVER')
        elif x == 'vermelha':
            print('Quando você abriu a porta, sentiu um calor insuportavel, mas ja não tinha mais como voltar, você morreu queimado!')
            print('GAME OVER')
        elif x == 'amarela':
            print('PARABENS VOCÊ CONSEGUIU ACHAR O TESOURO!!!')
        else:
            print('GAME OVER, NÃO TENTE COLOCAR OPÇÕES QUE NÃO EXISTE, SO TE LEVARA A MORTE')
    elif x =='passar':
        print('Você deveria ter esperado, tinha muitos crocodilos famintos so te esperando pular')
        print('GAME OVER')
    else:
        print('GAME OVER, NÃO TENTE COLOCAR OPÇÕES QUE NÃO EXISTE, SO TE LEVARA A MORTE')
elif x== 'direita':
    print('Você caiu em um buraco enorme, infelizmente não tem ninguem por perto, não adianta gritar, so resta esperar a morte')
    print('GAME OVER')
else:
    print('GAME OVER, NÃO TENTE COLOCAR OPÇÕES QUE NÃO EXISTE, SO TE LEVARA A MORTE')

    