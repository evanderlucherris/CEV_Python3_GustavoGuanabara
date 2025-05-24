'''
Python Exercise 013:
Create an algorithm that reads an employee’s salary and shows their new salary with a 15% raise.
'''

salario = float(input('Qual é o salário do funcionário: '))
novo = salario + (salario * 15 / 100)

print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo))