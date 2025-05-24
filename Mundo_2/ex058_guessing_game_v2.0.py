'''
Python Exercise 058:
Improve the game from CHALLENGE 28 where the computer “thinks” of a number between 0 and 10. 
Now the player will keep trying to guess until they get it right, 
showing at the end how many attempts were needed to win.
'''

from random import randint
computador = randint(0, 10)
palpites = 0
print('sou seu computador... Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))