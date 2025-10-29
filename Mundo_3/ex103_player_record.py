'''
Create a program that has a function called **record()**, which receives two optional parameters: 
the name of a player and how many goals they scored. The program must be able to display the player's record, 
even if some data has not been provided correctly.
'''
def ficha(nome='<desconhecido>', gols=0):
    """
    Mostra a ficha de um jogador de futebol.
    
    :param nome: nome do jogador (opcional)
    :param gols: número de gols marcados (opcional)
    """
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

# Programa principal
n = input('Nome do jogador: ').strip()
g = input('Número de gols: ').strip()

# Tratamento de valores vazios
if g.isnumeric():
    g = int(g)
else:
    g = 0

if n == '':
    ficha(gols=g)
else:
    ficha(n, g)
