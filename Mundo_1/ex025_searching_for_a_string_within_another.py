'''
Python Exercise 025:
Create a program that reads a person’s name and tells if they have "SILVA" in their name.
'''

nome = str(input('Qual é o seu nome completo? ')).strip()

print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))