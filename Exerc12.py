# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

nr_semana = int(input("Digite um número da semana: "))

if nr_semana == 1:
    print("Domingo")
elif nr_semana == 2:
    print('Segunda-Feira')
elif nr_semana == 3:
    print('Terça-feira')
elif nr_semana == 4:
    print('Quarta-feira')
elif nr_semana == 5:
    print('Quinta-feira')
elif nr_semana == 6:
    print('Sexta-feira')
elif nr_semana == 7:
    print('Sábado')
else:
    print('Dia da semana inválido!')