'''
in this lesson, we will continue our study of functions in python, 
learning more about interactive help in python, the use of docstrings to document our functions, 
optional arguments to give more dynamism to python functions, variable scope, and returning results.
'''
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

help(contador)

def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: sem retorno
    """
    s = a + b + c
    print(f'A soma vale {s}')
somar(3, 2, 5)
somar(8, 4)
somar()