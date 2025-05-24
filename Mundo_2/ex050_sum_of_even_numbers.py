'''
Python Exercise 050:
Develop a program that reads six integers and shows the sum of only those that are even. 
If a number entered is odd, ignore it.
'''

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} número(s) pare(s). E a soma foi {}'.format(cont, soma))