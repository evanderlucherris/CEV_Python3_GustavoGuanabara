'''
python exercise 088:
create a program to help a mega sena player generate guesses.
the program will ask how many games should be generated
and will randomly draw 6 numbers between 1 and 60 for each game,
storing everything in a nested list.
'''

from random import randint
from time import sleep
lista = []
jogos = []
print('=-'*30)
print('                   JOGA NA MEGASENA                ')
print('=-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('=-'*3, f'SORTEANDO {quant} JOGOS', '=-'*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*5, '< BOA SORTE >', '=-'*5)