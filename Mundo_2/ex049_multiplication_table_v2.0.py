'''
Python Exercise 049:
Redo CHALLENGE 9, showing the multiplication table of a number chosen by the user, 
but now using a for loop.
'''

num = int(input('Digite um número para ver a sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))

#ESSE EXERCÍCIO É UM APERFEIÇOAMENTO DO EX 009