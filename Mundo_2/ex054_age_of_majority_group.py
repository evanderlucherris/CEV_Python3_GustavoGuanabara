'''
Python Exercise 054:
Create a program that reads the birth year of seven people. 
At the end, show how many people are still underage and how many are adults.
'''

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
        nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
        idade = atual - nasc
        if idade >= 21:
                totmaior += 1
        else:
                totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E também tivemos {} pessoas menores de idade.'.format(totmenor))