'''
Python Exercise 065:
Create a program that reads multiple integers from the keyboard. 
At the end of execution, show the average of all values and the highest and lowest values read. 
The program should ask the user whether they want to continue entering values or not.
'''

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant ==1:
        menor = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a media foi {:.1f}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))