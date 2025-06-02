'''
python exercise 100: 
create a program that has a list called números and two functions called sorteia() and somaPar(). 
the first function will draw 5 numbers and put them inside the list, 
and the second function will show the sum of all the even values drawn by the previous function.
'''
from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0,5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')
numeros = list()
sorteia(numeros)
somaPar(numeros)