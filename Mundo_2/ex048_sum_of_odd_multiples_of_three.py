'''
Python Exercise 048:
Write a program that calculates the sum of all numbers that are multiples 
of three and are within the range from 1 to 500.
'''

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0 :
        soma += c #soma = soma + c
        cont += 1 #cont = cont + 1
print('A soma entre todos os {} valores solicitados é {}'.format(cont, soma))