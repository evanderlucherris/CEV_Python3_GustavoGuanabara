'''
Python Exercise 068:
Write a program that plays Even or Odd with the computer. 
The game will only stop when the player loses, 
showing the total number of consecutive wins the player achieved at the end of the game.
'''

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI': 
        tipo = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}. ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER. Você venceu {v} vezes')