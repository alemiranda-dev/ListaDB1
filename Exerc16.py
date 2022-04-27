# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não
# bissexto.

from calendar import isleap

ano = int(input("Digite um ano: "))

if isleap(ano):
    print('É bissexto')
else:
    print('Não é bissexto')