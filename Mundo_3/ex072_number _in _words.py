'''
Python Exercise 072:
Create a program that has a fully populated tuple with the written form of the numbers from zero to twenty. 
The program should read a number from the keyboard (between 0 and 20) and display it in words.
'''

cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
        'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
        'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
        'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente. ', end='')

    print(f'Você digitou o número {cont[num]}')

    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    if continuar != 'S':
        print('Programa encerrado.')
        break
