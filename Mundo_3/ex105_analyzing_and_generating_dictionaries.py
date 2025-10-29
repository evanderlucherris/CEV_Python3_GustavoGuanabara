'''
Create a program that has a function called grades(), 
which can receive multiple student grades and will return 
a dictionary with the following information:
– Number of grades
– Highest grade
– Lowest grade
– Class average
– Situation (optional)
'''
def notas(*notas, sit=False):
    """
    Função para analisar notas de alunos.
    
    :param notas: várias notas de alunos
    :param sit: (opcional) indica se a situação da turma será exibida
    :return: dicionário com quantidade, maior, menor, média e situação (opcional)
    """
    resultado = {}
    resultado['quantidade'] = len(notas)
    resultado['maior'] = max(notas) if notas else 0
    resultado['menor'] = min(notas) if notas else 0
    resultado['média'] = sum(notas)/len(notas) if notas else 0
    
    if sit:
        if resultado['média'] >= 7:
            resultado['situação'] = 'BOA'
        elif resultado['média'] >= 5:
            resultado['situação'] = 'RAZOÁVEL'
        else:
            resultado['situação'] = 'RUIM'
    
    return resultado

# Programa principal
resp = notas(8, 7.5, 9, 4, sit=True)
print(resp)
