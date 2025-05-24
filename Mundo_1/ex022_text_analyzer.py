'''
Python Exercise 022:
Create a program that reads a person’s full name and shows:
– The name in all uppercase and lowercase letters.
– The total number of letters (excluding spaces).
– How many letters the first name has.
'''

nome = str(input('Digite o seu nome completo: ')).strip()
dividido = nome.split()
print('Analisando o seu nome...')
print('O seu nome em maiúsculas é {}'.format(nome.upper()))
print('O seu nome em minúsculas é {}'.format(nome.lower()))
print('O seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(dividido[0], len(dividido[0])))

#print('Seu primeiro nome é {} e ele tem {} letras'.format(nome.find(' ')))