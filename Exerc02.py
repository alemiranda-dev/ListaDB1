# Faça um Programa que peça um valor e mostre na tela se o
#valor é positivo ou negativo.

valor = int(input("Digite um valor: "))

if valor == 0:
    print("Zero é neutro")
elif valor > 1:
    print("Positivo")
else:
    print("Negativo")
