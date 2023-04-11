print('Bem vindo a calculadora de gorjeta')
x = float(input('Qual o valor total da compra: '))
y = int(input('Quantas pessoas vão dividir a conta: '))
z = int(input('Qual o valor da porcentagem da gorjeta: '))

gorjeta = (x*(100-(100-z)))/100
total = round((x+gorjeta)/y,2)
print(f'O valor total que cada pessoa ira pagar é {total}')