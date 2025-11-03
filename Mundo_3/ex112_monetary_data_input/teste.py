''''
Inside the **utilidadesCeV** package we created in challenge #111, 
we have a module called **dado**. Create a function called **readMoney()** 
that works like the **input()** function, but with data validation to 
accept only values that are monetary.
'''

from utilidadescev import moeda
from utilidadescev import dado

p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 20, 11)
