'''
Python Exercise 051:
Develop a program that reads the first term and the common difference 
of an arithmetic progression (AP). 
At the end, display the first 10 terms of this progression.
'''

print('=' * 30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('=' * 30)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' → ')
print('ACABOU!')