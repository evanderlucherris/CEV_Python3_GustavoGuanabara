'''
Python Exercise 011:
Write a program that reads the width and height of a wall in meters, 
calculates its area, and the amount of paint needed to paint it, 
knowing that each liter of paint covers 2 square meters.
'''

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2

print('Sua parede tem a dimensão de {}x{} e a área é de {}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))