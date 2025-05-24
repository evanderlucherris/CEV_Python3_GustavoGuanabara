'''
Python Exercise 020:
The same teacher from exercise 19 wants to randomly determine the order of student presentations. 
Write a program that reads the names of four students and displays the randomized order.
'''

from random import shuffle
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
shuffle(lista)

print('A ordem de apresentação será ')
print(lista)