'''
Create a program that has a function called vote(), which will receive as a parameter a person's year of birth,
returning a literal value indicating whether the person has their vote DENIED, OPTIONAL,
or MANDATORY in the elections.
'''

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    
#Programa Principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))