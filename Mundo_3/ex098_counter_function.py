'''
python exercise 098: 
create a program that has a function called contador(), 
which receives three parameters: 
start, end, and step. 
your program must perform three counts using the created function:
a) from 1 to 10, counting by 1
b) from 10 to 0, counting by 2
c) a customized count
'''
from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1 
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.0)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM!')


#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é a sua vez de personalizar a contagem: ')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)