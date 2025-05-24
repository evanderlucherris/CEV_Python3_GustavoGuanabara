'''
Python Exercise 061:
Redo CHALLENGE 51, reading the first term and the common difference of an arithmetic progression (AP), 
showing the first 10 terms of the progression using a while loop.
'''

print('GERADOR DE PA')
print('=-' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')