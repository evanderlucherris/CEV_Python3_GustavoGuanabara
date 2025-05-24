'''
Python Exercise 033:
Write a program that reads three numbers and shows which one is the greatest and which one is the smallest.
'''

'''n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('terceiro valor: '))
lista = n1, n2, n3

print('O MAIOR número digitado foi {}'.format(max(lista)))
print('O MENOR número digitado foi {}'.format(min(lista)))'''

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
menor = n1
maior = n1
#VERIFICANDO QUEM É O MENOR
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#VERIFICANDO QUEM É O MAIOR
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3 
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))