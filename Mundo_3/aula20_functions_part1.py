'''
in this lesson, we will learn what functions or routines are and how to use functions in python. 
functions are pieces of code that can be executed at different moments in our python programs. 
see how the def command works in python and how to use it with simple and multiple parameters.
'''

def lin():
    print('-' * 30)
#----------------------------------------- Primeiro comando
def titulo(txt):
    print('-' *30)
    print(txt)
    print('-' * 30)
#----------------------------------------- Segundo comando
def soma(a, b):
    s = a + b
    print(s)
#----------------------------------------- Terceiro comando
#Programa principal
lin()
print('    CURSO EM VÍDEO    ')
lin()
print('    APRENDA PYTHON    ')
lin()
print('    GUSTAVO GUANABARA    ')
lin()
#----------------------------------------- Divisão de comandos
titulo('    CURSO EM VÍDEO    ')
titulo('    APRENDA PYTHON    ')
titulo('    GUSTAVO GUANABARA    ')
#----------------------------------------- Divisão de comandos
soma(4, 5)
soma(8, 9)
soma(2, 1)