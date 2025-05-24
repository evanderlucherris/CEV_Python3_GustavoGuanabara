'''
Python Exercise 023:
Write a program that reads a number from 0 to 9999 and displays each of the digits separately.
'''

num = int(input('Digite um número de 0 à 9999: '))
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(num // 1 % 10))
print('Dezena: {}'.format(num //10 % 10))
print('Centena: {}'.format(num //100 % 10))
print('Milhar: {}'.format(num //1000 % 10))