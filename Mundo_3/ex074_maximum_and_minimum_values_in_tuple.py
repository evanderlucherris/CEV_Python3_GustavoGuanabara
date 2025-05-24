'''
Python Exercise 074:
Create a program that will generate five random numbers and store them in a tuple. 
After that, display the list of generated numbers and also indicate the smallest and the largest values in the tuple.
'''

from random import randint 
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)) 
print('Os valores sorteados foram: ', end='')
for n in num:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')