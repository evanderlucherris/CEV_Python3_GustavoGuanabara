'''
Python Exercise 077:
Create a program that has a tuple with several words (do not use accents).
After that, you must display, for each word, which vowels it contains.
'''

palavras = ('aprender', 'programar', 'linguagem', 'python'
            'curso', 'gratis', 'estudar', 'prticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')