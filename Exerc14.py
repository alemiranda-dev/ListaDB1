# Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
# um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

lado1 = int(input("Digite o Lado 1: "))
lado2 = int(input("Digite o Lado 2: "))
lado3 = int(input("Digite o Lado 3: "))

if lado1 == lado2 == lado3:
    print("Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Isósceles")
elif lado1 != lado2 != lado3:
    print("Escaleno")