'''
Python Exercise 018:
Write a program that reads any angle and displays the sine, cosine, and tangent values of that angle.
'''

from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))
rad = radians(ang)

print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sin(rad)))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cos(rad)))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(ang, tan(rad)))