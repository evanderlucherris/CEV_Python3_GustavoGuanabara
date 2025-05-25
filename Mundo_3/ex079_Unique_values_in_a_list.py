'''
Python Exercise 079: 
Create a program where the user can enter several numeric values and store them in a list. 
If the number already exists in the list, it should not be added. In the end, 
display all the unique values entered, in ascending order.
'''

numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('=-'*30)
numeros.sort()
print(f'Você digitou os valores {numeros}')