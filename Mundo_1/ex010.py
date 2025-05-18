real = float(input('Quanto de dinheiro você tem na carteira: R$ '))
dolar = real / 5.70
euro = real / 5.98

print('Com R${} você pode comprar US${:.2f} ou €{:.2f}'.format(real, dolar, euro))