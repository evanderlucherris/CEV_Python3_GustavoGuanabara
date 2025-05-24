'''
Python Exercise 028:
Write a program that makes the computer “think” of an integer between 0 and 5 
and asks the user to try to guess the number chosen by the computer. 
The program should display whether the user won or lost.
'''

from random import randint
from time import sleep
computador = randint(1, 5) #FAZ O COMPUTADOR "PENSAR"

print('-=-' * 20)
print('VOU PENSAR EM UM NÚMERO DE 0 - 5. TENTE ADIVINHAR...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei? ')) #JOGADOR TENTA ADIVINHAR O NÚMERO
print('PROCESSANDO...')
sleep(2)

if jogador == computador:
    print('Parabéns! Você você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador, jogador))