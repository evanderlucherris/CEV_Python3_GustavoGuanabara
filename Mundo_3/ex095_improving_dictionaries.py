'''
python exercise 095: 
improve challenge 93 so that it works with multiple players, 
including a system to view detailed performance of each player.
'''

'''
python exercise 093: create a program that manages the performance of a soccer player. 
the program will read the player's name and how many matches they played. 
then it will read the number of goals scored in each match. 
in the end, all of this will be stored in a dictionary, 
including the total number of goals scored during the championship.
'''

time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('=-'*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('=-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):>15}', end='')
    print()
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'    -- LEVANTAMENTO DO JOGADOR |{time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]('gols ')):
            print(f'    No jogo {i+1} fez {g} gols')
    print('=-'*40)
print('<< VOLTE SEMPRE >>')