'''
Create a module called **money.py** that contains the built-in functions 
**increase()**, **decrease()**, **double()**, and **half()**. 
Also, create a program that imports this module and uses some of these functions.
'''

import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {p:.2f} é R$ {moeda.metade(p):.2f}')
print(f'O dobro de R$ {p:.2f} é R$ {moeda.dobro(p):.2f}')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(p, 10):.2f}')