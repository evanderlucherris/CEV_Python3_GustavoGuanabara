'''
in this lesson, we will continue our study of functions in python, 
learning more about interactive help in python, the use of docstrings to document our functions, 
optional arguments to give more dynamism to python functions, variable scope, and returning results.
'''
def contador(i, f, p):
    """
    -> |Faz uma contagem e mostra na tela.
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