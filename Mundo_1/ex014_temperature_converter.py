'''
Python Exercise 014:
Write a program that converts a temperature entered in degrees Celsius to degrees Fahrenheit.
'''

c = float(input('informe a temperatura em °C: '))
f = 9 * c / 5 + 32

print('A temperatua de {}°C corresponde a {}°F!'.format(c, f))