'''
Python Exercise 082:
Create a program that will read several numbers and store them in a list.
After that, create two additional lists that will contain only the even and the odd numbers entered, respectively.
At the end, display the contents of all three generated lists.
'''

num = []
pares = []
impares = []
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('=-'*30)
print(f'A lista completo é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')