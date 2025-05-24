'''
Python Exercise 030:
Create a program that reads an integer and shows on the screen whether it is EVEN or ODD.
'''

num = int(input('Me diga um número qualquer: '))

if num % 2 == 0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é ÍMPAR'.format(num))