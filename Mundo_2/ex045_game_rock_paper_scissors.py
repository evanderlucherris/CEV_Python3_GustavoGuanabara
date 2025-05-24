'''
Python Exercise 045:
Create a program that lets the computer play Rock-Paper-Scissors (Jokenpô) with you.
'''

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções:
      [ 0 ]Pedra
      [ 1 ]Papel
      [ 3 ]Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

if computador == 0: #PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Jogador VENCE!')
    elif jogador == 2:
        print('Computador VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: #PAPEL
    if jogador == 0:
        print('Computador VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Jogador VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: #TESOURA
    if jogador == 0:
        print('Jogador VENCE!')
    elif jogador == 1:
        print('Computador VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
