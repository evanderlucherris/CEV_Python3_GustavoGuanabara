'''
Python Exercise 057:
Write a program that reads a person’s gender, but only accepts the values ‘M’ or ‘F’. 
If the input is incorrect, keep asking until a valid value is entered.
'''

sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))