'''
Python Exercise 036:
Write a program to approve a bank loan for the purchase of a house. 
Ask the user for the value of the house, the buyer’s salary, 
and in how many years they intend to pay it off.
The monthly installment cannot exceed 30% of the buyer’s salary; 
otherwise, the loan will be denied.
'''

casa = float(input('Valor da casa? R$'))
salario = float(input('Salário do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos,'.format(casa, anos), end=' ')
print('a prestação será de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO.')