# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

from datetime import datetime

data = input("Digite uma data no formato dd/mm/aaaa: ")
print("A data digitada é: " + str(data))
formatacao = "%d/%m/%Y"
res = True
try:
    res = bool(datetime.strptime(data, formatacao))
except ValueError:
    res = False

print("Data válida? : " + str(res))
