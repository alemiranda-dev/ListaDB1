# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades
# do mesmo.

numero = int(input("Digite um número de 0 a 1000: "))

centena = numero // 100
dezena = (numero - centena * 100) // 10
unidade = numero - centena * 100 - dezena * 10


if numero < 1000:
  print(f"\n Esse número possui: \n"
        f"\n {centena} centena(s) \n"
        f"\n {dezena} dezena(s) \n"
        f"\n {unidade} unidade(s) \n")
else:
  print("Número inválido!")