'''
Python Exercise 008:
Write a program that reads a value in meters and displays it converted to centimeters and millimeters.
'''

medida = float(input('Uma distância em metros: '))

print('O valor de {:.0f}m, equivale a \n{:.0f}cm \n{:.0f}mm \n{:.0f}dam \n{:.1f}km \n{:.0f}dm \n{:.0f}hm \n{:.0f}m'
      .format(medida, (medida*100), (medida*1000), (medida/10), (medida/1000), (medida*10), (medida/100), (medida)))