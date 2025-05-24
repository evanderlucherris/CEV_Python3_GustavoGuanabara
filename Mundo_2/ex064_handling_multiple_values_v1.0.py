'''
Python Exercise 064:
Create a program that reads multiple integers from the keyboard. 
The program will only stop when the user enters the value 999, which is the stop condition. 
At the end, show how many numbers were entered and the sum of them (excluding the stop flag).
'''

num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('você digitou {} números e a soma entre eles foi {}'.format(cont, soma))