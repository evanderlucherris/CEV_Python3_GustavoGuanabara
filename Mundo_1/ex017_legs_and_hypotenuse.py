'''
Python Exercise 017:
Write a program that reads the length of the opposite and adjacent legs of a right triangle. 
Calculate and display the length of the hypotenuse.
'''

'''
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

print('A hipotenusa vai medir {:.2f}'.format(hypot(co, ca)))
'''
'''
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hi))
'''
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))