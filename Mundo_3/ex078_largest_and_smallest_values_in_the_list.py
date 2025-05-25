'''
Python Exercise 078: Write a program that reads 5 numeric values and stores them in a list. 
At the end, show which was the largest and the smallest value entered 
and their respective positions in the list.
'''

listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'O MAIOR valor foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O MENOR valor foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()