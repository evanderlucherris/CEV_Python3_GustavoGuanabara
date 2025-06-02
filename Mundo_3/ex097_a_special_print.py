'''
python exercise 097: 
create a program that has a function called escreva(), 
which receives any text as a parameter and displays a message with an adaptable size.
example:
escreva('hello, world!')
'''

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


#PROGRAMA PRINCIPAL:
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')