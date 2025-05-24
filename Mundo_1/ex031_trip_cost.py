'''
Python Exercise 031:
Develop a program that asks for the distance of a trip in kilometers. 
Calculate the ticket price, charging R$0.50 per km for trips up to 200 km and R$0.45 for longer trips.
'''

'''distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}Km.'.format(distancia))

if distancia <= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(distancia * 0.50))
else:
    print('E o valor da sua passagem será de R${:.2f}'.format(distancia * 0.45))'''

distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}Km.'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o valor da sua passagem será de R${:.2f}'.format(preco))