dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos KM rodados? '))
total = 0.15 * km + dias * 60

print('O total a pagar é de R${:.2f}'.format(total))