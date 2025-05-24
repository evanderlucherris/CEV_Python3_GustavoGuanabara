'''
Python Exercise 043:
Develop a program that reads a person’s weight and height, calculates their Body Mass Index (BMI), 
and shows their status according to the table below:
BMI below 18.5: Underweight
Between 18.5 and 25: Ideal Weight
25 to 30: Overweight
30 to 40: Obesity
Above 40: Morbid Obesity
'''

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura: (m) '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('o IMC dessa pessoa é de {:.1f}'.format(imc))
    print('Você está ABAIXO DO PESO normal.')
elif imc < 25:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('PARABÉNS, você está na faixa de PESO NORMAL.')
elif imc < 30:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('Você está em SOBREPESO.')
elif imc < 40:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('Você está em OBESIDADE.')
else:
    print('O IMC desta pessoa é de {:.1f}'.format(imc))
    print('Você está em OBESIDADE MORBIDA, cuidado.')