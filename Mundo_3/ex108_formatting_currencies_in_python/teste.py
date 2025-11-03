'''
Adapt the code from challenge #107, creating an additional function called **currency()** 
that can display numbers as a formatted monetary value.

'''

import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {moeda.moeda(p)} é R$ {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de R$ {moeda.moeda(p)} é R$ {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos R$ {moeda.moeda(moeda.aumentar(p, 10))}')