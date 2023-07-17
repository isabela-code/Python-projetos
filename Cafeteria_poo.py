class Cafe:
    def __init__(self):
        self.Maquina_ligada = True
        self.codigo = False
        self.leite = 500
        self.agua = 500
        self.cafe = 500
        self.expresso = 1.50
        self.latte = 2.50
        self.cappuccino = 3.50

    def escolha(self, escolha):
        if escolha == 'expresso':
            print('Seu expresso esta sendo feito, aguarde um momento')
        elif escolha == 'latte':
            print('Seu latte sendo feito, aguarde um momento')
        elif escolha == 'cappuccino':
            print('Seu cappuccino sendo feito, aguarde um momento')
        else:
            return 0

    def desligar(self,codigo):
        if codigo == True:
            print('Sua maquina de cafe foi desligada')
            self.Maquina_ligada = False
        else:
            print('Sua maquina de cafe ainda esta ligada e ficara assim')
            self.Maquina_ligada = True

    def relatorio(self):
        print(f'Tem {self.leite} ml de leite')
        print(f'Tem {self.agua} ml de agua')
        print(f'Tem {self.cafe} g de cafe')

    def fazer_cafe(self, escolha):
        if escolha == 'expresso':
            if self.agua >= 50 and self.leite >= 0 and self.cafe >= 18:
                self.leite -= 0
                self.agua -= 50
                self.cafe -= 18
                Cafe().pagar(escolha)
                Cafe().escolha(escolha)
                Cafe().concluido()
            elif self.agua < 50 and self.leite < 0 and self.cafe < 18:
                print('Infelizmente não temos estoque para nenhum dos cafes')
            else:
                print('Infelizmente não temos estoque para fazer mais expresso')
        elif escolha == 'latte':
            if self.agua >= 200 and self.leite >= 150 and self.cafe >= 24:
                self.leite -= 150
                self.agua -= 200
                self.cafe -= 24
                Cafe().pagar(escolha)
                Cafe().escolha(escolha)
                Cafe().concluido()
            elif self.agua < 50 and self.leite < 0 and self.cafe < 18:
                print('Infelizmente não temos estoque para nenhum dos cafes')
            else:
                print('Infelizmente não temos estoque para fazer mais latte')
        elif escolha == 'cappuccino':
            if self.agua >= 250 and self.leite >= 100 and self.cafe >= 24:
                self.leite -= 100
                self.agua -= 250
                self.cafe -= 24
                Cafe().pagar(escolha)
                Cafe().escolha(escolha)
                Cafe().concluido()
            elif self.agua < 50 and self.leite < 0 and self.cafe < 18:
                print('Infelizmente não temos estoque para nenhum dos cafes')
            else:
                print('Infelizmente não temos estoque para fazer mais cappuccino')
    def pagar(self,escolha):
        if escolha == 'expresso':
            print(f'O preço da sua bebida é de R$ {self.expresso}')
        elif escolha == 'latte':
            print(f'O preço da sua bebida é de R$ {self.latte}')
        elif escolha == 'cappuccino':
            print(f'O preço da sua bebida é de R$ {self.cappuccino}')
        y = int(input('Quantas moedas de R$ 0.05 você ira colocar na maquina: '))
        z = int(input('Quantas moedas de R$ 0.10 você ira colocar na maquina: '))
        w = int(input('Quantas moedas de R$ 0.25 você ira colocar na maquina: '))
        f = int(input('Quantas moedas de R$ 0.50 você ira colocar na maquina: '))
        u = int(input('Quantas moedas de R$ 1.00 você ira colocar na maquina: '))
        soma = (0.05 * y) + (0.10 * z) + (0.25 * w) + (0.50 * f) + (1 * u)
        print(f'Você colocou R$ {soma}')
        if self.expresso > soma:
            print('Parece que você não tem dinheiro o suficiente')
        elif self.latte > soma:
            print('Parece que você não tem dinheiro o suficiente')
        elif self.cappuccino > soma:
            print('Parece que você não tem dinheiro o suficiente')
        if soma > self.expresso and escolha == 'expresso':
            troco = soma - self.expresso
            print(f"Seu troco é de {troco}")
        elif soma > self.latte and escolha == 'latte':
            troco = soma - self.latte
            print(f"Seu troco é de {troco}")
        elif soma > self.cappuccino and escolha == 'cappuccino':
            troco = soma - self.cappuccino
            print(f"Seu troco é de {troco}")

    def checar(self):
        if self.agua < 50 and self.leite < 0 and self.cafe < 18:
            print('Infelizmente não temos estoque para nenhum dos cafes')
        elif self.agua < 200 and self.leite < 150 and self.cafe < 24:
            print('Infelizmente a bebida latte e cappuccino saiu do estoque por hoje')
        else:
            return

    def concluido(self):
        desenho = '''
            {   }  {
            }_{ __{
         .-{   }   }-.
        (   }     {   )
        |`-.._____..-'|
        |             ;--.
        |            (__  )
        |             | )  )
        |             |/  /
        |             /  /  
        |            (  /
        \             y'
          `-.._____..-' 
        '''
        print('Aqui esta sua bebida')
        print(desenho)