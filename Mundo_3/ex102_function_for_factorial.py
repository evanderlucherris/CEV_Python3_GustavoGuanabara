'''
Create a program that has a function called **factorial()** which receives two parameters: 
the first indicating the number to be calculated, and another called **show**, 
which will be an optional boolean value indicating whether or not the factorial 
calculation process will be displayed on the screen.
'''

def fatorial(n, show=False):
    """
    Calcula o fatorial de um número.
    
    :param n: número a ser calculado
    :param show: (opcional) mostra ou não o processo de cálculo
    :return: o valor do fatorial de n
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
    return f

# Exemplos de uso:
print(fatorial(5, show=True))   # Mostra o cálculo
print(fatorial(5))              # Só mostra o resultado
