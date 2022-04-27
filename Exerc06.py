# Faça um Programa que leia três números e mostre o maior e o menor deles.

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

if valor1 > valor2 and valor1 > valor3:
    print(f"Maior valor {valor1}")
    if valor3 > valor2:
        print(f"Menor valor {valor2}")
    else:
        print(f"Menor valor {valor3}")
elif valor2 > valor3 and valor2 > valor1:
    print(f"Maior valor {valor2}")
    if valor3 > valor1:
        print(f"Menor valor {valor1}")
    else:
        print(f"Menor valor {valor3}")
elif valor3 > valor1 and valor3 > valor2:
    print(f"Maior valor {valor3}")
    if valor1 > valor2:
        print(f"Menor valor {valor2}")
    else:
        print(f"Menor valor {valor1}")