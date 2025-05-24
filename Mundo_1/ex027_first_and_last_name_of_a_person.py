'''
Python Exercise 027:
Write a program that reads a person’s full name, then displays the first and last name separately.
'''

'''nome = str(input('Digite o seu nome completo: ')).strip().split()
print('Muito prazer em te conhecer!')

print('O seu primeiro nome é {}'.format(nome[0]))
print('O seu último nome é {}'.format(nome[-1]))'''

n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split()
print('Prazer em te conhecer!')
print('O seu primeiro nome é {}'.format(nome[0]))
print('O seu último nome é {}'.format(nome[len(nome) - 1]))