from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
if idade < 18:
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
    saldo = idade - 18
    print('Já deveria ter se alistado à {} anos.'.format((saldo)))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
elif idade == 18:
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
    print('Você tem que alistar IMEDIATAMENTE.')
