'''
Python Exercise 009:
Write a program that reads any integer and displays its multiplication table.
'''

num = int(input('Digite um número para ver a sua tabuada: '))

'''
print('{} x  1 = {} \n{} x  2 = {} \n{} x  3 = {} \n{} x  4 = {} \n{} x  5 = {}'
      '\n{} x  6 = {} \n{} x  7 = {} \n{} x  8 = {} \n{} x  9 = {} \n{} x 10 = {}'
      .format((num), (num*1), (num), (num*2), (num), (num*3), (num), (num*4), (num), (num*5),
              (num), (num*6), (num), (num*7), (num), (num*8), (num), (num*9), (num), (num*10)))
'''
print('-' * 12)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('-' *12)