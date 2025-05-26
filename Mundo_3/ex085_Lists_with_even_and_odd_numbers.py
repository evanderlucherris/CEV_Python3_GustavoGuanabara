'''
Python Exercise 085:
Create a program where the user can enter seven numeric values
and store them in a single list that keeps even and odd values separated.
In the end, display the even and odd values in ascending order.
'''

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('=-'*30)
num[0].sort()
num[1].sort()
print(f'Todos os valores {num}')
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')