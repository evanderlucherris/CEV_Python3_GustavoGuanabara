'''
Python Exercise 063:
Write a program that reads any integer N and displays the first N elements of the Fibonacci sequence. 
Example:
0 – 1 – 1 – 2 – 3 – 5 – 8
'''

print('-' * 30)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print('{} → {}'.format(t1, t2), end=' ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('→ {}'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('→ FIM')
print('~' * 30)