'''
Python Exercise 066:
Create a program that reads integers from the keyboard. 
The program will only stop when the user enters the value 999, which is the stop condition. 
At the end, show how many numbers were entered and the sum of them (excluding the stop flag).
'''

num = cont = soma = 0
while num != 999:
    num = int(input('Digite um valor [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores é {soma}')