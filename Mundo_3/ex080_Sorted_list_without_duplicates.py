'''
Python Exercise 080: 
Create a program where the user can enter five numeric values and insert
 them into a list in the correct sorted position (without using sort()). 
 In the end, display the sorted list on the screen.
'''

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('=-'*30)
print(f'Os valores digitados em ordem foram {lista}')