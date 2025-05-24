'''
Python Exercise 038:
Write a program that reads two integers and compares them, displaying a message on the screen:
The first value is greater
The second value is greater
There is no greater value, both are equal
'''

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

if n1 > n2:
    print('O PRIMEIRO valor é MAIOR.')
elif n2 > n1:
    print('O SEGUNDO valor é MAIOR.')
else:
    print('Os DOIS valores são IGUAIS.')