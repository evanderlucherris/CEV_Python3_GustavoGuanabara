'''
Python Exercise 012:
Create an algorithm that reads the price of a product and shows its new price with a 5% discount.
'''

preco = float(input('Qual o preço do produto? '))
desc = preco - (preco * 5 / 100)

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, desc))