salario = float(input('Qual é o salário do funcionário: R$'))

if salario <= 1250.00:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, salario * 15 / 100 + salario))
else:
    print('Quam ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, salario * 10 / 100 + salario))