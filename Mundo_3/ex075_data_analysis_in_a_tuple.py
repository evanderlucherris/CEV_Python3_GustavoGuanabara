'''
Python Exercise 075:
Develop a program that reads four values from the keyboard and stores them in a tuple. At the end, display:

A) How many times the number 9 appeared.
B) The position where the first number 3 was entered.
C) Which numbers are even.
'''

num = (int(input('Digite um número: ')),
        int(input('Digite um número: ')),
          int(input('Digite um número: ')),
            int(input('Digite um número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 apareceu em {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nunhuma posição')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')