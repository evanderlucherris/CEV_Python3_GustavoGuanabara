'''
Python Exercise 015:
Write a program that asks for the number of kilometers traveled by a rented car and the number of days it was rented. 
Calculate the amount to pay, knowing that the car costs R$60 per day and R$0.15 per kilometer driven.
'''

dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos KM rodados? '))
total = 0.15 * km + dias * 60

print('O total a pagar é de R${:.2f}'.format(total))