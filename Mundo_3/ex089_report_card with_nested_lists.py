'''
python exercise 089:
create a program that reads the name and two grades of several students and stores everything in a nested list.
at the end, display a report card showing each student’s average
and allow the user to view the individual grades of each student.
'''

ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('=-'*30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('=-'*30)
for i, a in enumerate(ficha):
    print(f'{i:4<}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('=-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 Interrompe)'))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')