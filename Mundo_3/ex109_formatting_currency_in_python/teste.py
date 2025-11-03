'''
Modify the functions created in challenge #107 so that they accept one additional parameter,
indicating whether the value returned by them should be formatted by the **currency()** 
function developed in challenge #108.

'''

import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {moeda.moeda(p)} é R$ {moeda.metade(p, True)}')
print(f'O dobro de R$ {moeda.moeda(p)} é R$ {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos R$ {moeda.diminuir(p, 13, True)}')