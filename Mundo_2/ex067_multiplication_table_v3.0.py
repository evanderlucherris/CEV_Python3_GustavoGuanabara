'''
Python Exercise 067:
Write a program that shows the multiplication table of several numbers, 
one at a time, for each value entered by the user. 
The program will be interrupted when a negative number is requested.
'''

while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADA. VOLTE SEMPRE!')