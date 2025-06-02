'''
python exercise 096: create a program that has a function called area(), 
which receives the dimensions of a rectangular land (width and length) 
and displays the area of the land.
'''

def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')

#PROGRAMA PRINCIPAL:
print('  Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)