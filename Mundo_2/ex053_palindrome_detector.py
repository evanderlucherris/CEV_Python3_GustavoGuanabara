'''
Python Exercise 053:
Create a program that reads any phrase and tells if it is a palindrome, 
ignoring spaces. Examples of palindromes:
"AFTER THE SOUP",
"THE HOUSE’S PORCH",
"THE TOWER OF DEFEAT",
"THE WOLF LOVES THE CAKE",
"THE MARATHON DATE WAS NOTED".
'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, - 1, - 1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um Palíndromo')
else:
    print('A frase digitada não é um Palíndromo!')