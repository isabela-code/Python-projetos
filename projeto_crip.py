letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
codigo = input('Você deseja codificar ou decodificar a sua mensagem: ')
texto = input('Digite sua mensagem: ').lower()
digito = int(input('Digite um numero de 0 a 25: '))
posi = letras[0]
novo = []
z = []

for i in range(digito, 26):
    posi = letras[i]
    novo += posi
for i in range(0, digito):
    posi = letras[i]
    novo += posi

if codigo == 'codificar':
    for i in texto:
        a = 0
        for s in letras:
            if i == s:
                z.append(a)
            a += 1
    posit = novo[0]
    crip = []
    for i in z:
        posit = novo[i]
        crip.append(posit)
    cript = ''
    for i in crip:
        cript += i
    print(f'Sua mensagem codificada é {cript}')

if codigo == 'decodificar':
    for i in texto:
        a = 0
        for s in novo:
            if i == s:
                z.append(a)
            a += 1
    posit = letras[0]
    dcrip = []
    for i in z:
        posit = letras[i]
        dcrip.append(posit)
    dcript = ''
    for i in dcrip:
        dcript += i
    print(f'Sua mensagem codificada é {dcript}')