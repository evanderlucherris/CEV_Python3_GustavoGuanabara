print('{:=^40}'.format('LOJAS EVANDER'))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
      [ 1 ] À vista dinheiro/cheque
      [ 2 ] À vista cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a sua opção? '))
if opcao == 1:
    desc_din_cheq = preco - preco * 10 / 100
    print('Sua compra de R${:.2f}, vai custar R${:.2f} com 10% de desconto no final.'.format(preco, desc_din_cheq))
elif opcao == 2:
    desc_avista_cartao = preco - preco * 5 / 100
    print('Sua compra de R${:.2f}, vai custar R${:.2f} com 5% de desconto no final.'.format(preco, desc_avista_cartao))
elif opcao == 3:
    sem_juros = preco / 2
    print('Sua compra de R${:.2f}, vai ficar em 2 parcelas de R${:.2f} sem juros no final.'.format(preco, sem_juros))
elif opcao == 4:
    juros = preco + preco * 20 / 100
    parcelas = int(input('Quantas parcelas? '))
    if parcelas:
        print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcelas, juros / parcelas))
else:
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente.')