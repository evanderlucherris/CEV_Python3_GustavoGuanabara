'''
python exercise 090:
write a program that reads a student's name and average grade, 
also storing their status in a dictionary. 
at the end, display the contents of the structure on the screen.
'''

aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'