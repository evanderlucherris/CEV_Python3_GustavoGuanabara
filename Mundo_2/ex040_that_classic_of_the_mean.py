'''
Python Exercise 040:
Create a program that reads two grades of a student and calculates their average, 
showing a message at the end according to the average:
Average below 5.0: FAILED
Average between 5.0 and 6.9: RECOVERY
Average 7.0 or above: PASSED
'''

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
    print('O aluno está REPROVADO.')
elif media >= 5 and media < 6.9:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
    print('O aluno está de RECUPERAÇÃO.')
else:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
    print('O aluno está APROVADO.')