numeros = [1, 2, 3, 4, 5, 4.5]
frutas = ['banana', 'maça', 'abacaxi']

for num in numeros:
    print(num)

soma = 0
for num in numeros:
    soma += num
    print("Soma:", soma)

contador = 0
for _ in numeros:
    contador += 1
    print('Quantidade:', contador)

maior = numeros[0]
for num in numeros:
    if num > maior:
        maior = num
print('Maior:', maior)

quadrado = []
for i in range(1, 11):
    quadrado.append( i * i)
print(quadrado)

for i in numeros:
    if i % 2 == 0:
        print(i)

i = 0
for i in range(len(frutas)):
    print(len(frutas[i]))
    i += 1

dobro = []
for i in range(len(numeros)):
    dobro.append(numeros[i] * 2)
    print(dobro)

cont = float(input('insira um número:'))
for i in range(len(numeros)):
    posi = numeros[i]
    if cont == posi:
        print('Esse número está na lista!')
        break
count = 0
for num in numeros:
    if num % 2 == 0:
        count += 1
print('A quantidade de numetos pares é:', count)










