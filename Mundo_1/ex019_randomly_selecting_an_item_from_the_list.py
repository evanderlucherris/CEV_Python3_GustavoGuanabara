'''
Python Exercise 019:
A teacher wants to randomly select one of their four students to erase the board. 
Write a program to help them by reading the students names' and displaying the name of the chosen one.
'''

import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
sort = [a1, a2, a3, a4]

print('O aluno escolhido foi {}'.format(random.choice(sort)))