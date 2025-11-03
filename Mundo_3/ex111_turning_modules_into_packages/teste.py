''''
Create a package called **utilidadesCeV** that contains two internal modules 
named **moeda** and **dado**. Move all the functions used in challenges #107, 
#108, and #109 into the first module and keep everything working.

'''

from utilidadescev.moeda import moeda

p = float(input('Digite o preço: R$ '))
moeda.resumo(p, 20, 11)
