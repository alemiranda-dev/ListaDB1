# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input("Digite o preço do primeiro produto: "))
produto2 = float(input("Digite o preço do segundo produto: "))
produto3 = float(input("Digite o preço do terceiro produto: "))

if produto1 < produto2 and produto1 < produto3:
    print(f'Recomendamos o produto com o valor de R$ {produto1:.2f}')
elif produto2 < produto3 and produto2 < produto1:
    print(f'Recomendamos o produto com o valor de R$ {produto2:.2f}')
elif produto3 < produto2 and produto3 < produto1:
    print(f'Recomendamos o produto com o valor de R$ {produto3:.2f}')
