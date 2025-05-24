'''
Python Exercise 016:
Create a program that reads any real number from the keyboard and displays its integer part.
'''

'''
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))
'''
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))