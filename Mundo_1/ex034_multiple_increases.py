'''
Python Exercise 034:
Write a program that asks for an employee’s salary and calculates the amount of their raise. 
For salaries above R$1250.00, calculate a 10% raise. 
For salaries equal to or below that, the raise is 15%.
'''

salario = float(input('Qual é o salário do funcionário: R$'))

if salario <= 1250.00:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, salario * 15 / 100 + salario))
else:
    print('Quam ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, salario * 10 / 100 + salario))