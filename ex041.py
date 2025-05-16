from datetime import date

ano = int(input('Ano de nascimento: '))
classe = ['MIRIM', 'INFANTIL', 'JÚNIOR', 'SÊNIOR', 'MASTER']
idade = date.today().year - ano
if idade <= 9:
    print('O atleta tem {} anos.'.format(idade))
    print('CLASSIFICAÇÃO: {}'.format(classe[0]))
elif idade <= 14:
    print('O atleta tem {} anos.'.format(idade))
    print('CLASSIFICAÇÃO: {}'.format(classe[1]))
elif idade <= 19:
    print('O atleta tem {} anos.'.format(idade))
    print('CLASSIFICAÇÃO: {}'.format(classe[2]))
elif idade <= 25:
    print('O atleta tem {} anos.'.format(idade))
    print('CLASSIFICAÇÃO: {}'.format(classe[3]))
else:
    print('O atleta tem {} anos.'.format(idade))
    print('CLASSIFICAÇÃO: {}'.format(classe[4]))