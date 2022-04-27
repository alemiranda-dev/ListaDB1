# Ler três números e mostrá-los em ordem decrescente

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > n2:
    if n1 > n3:
        if n2 > n3:
            print(f'Ordem decrescente: {n1, n2, n3}')
        else:
            print(f'Ordem decrescente: {n1, n3, n2}')
    else:
        print(f'Ordem decrescente: {n3, n1, n2}')
else:
    if n2 > n3:
        if n1 > n3:
            print(f'Ordem decrescente: {n2, n1, n3}')
        else:
            print(f'Ordem decrescente: {n2, n3, n1}')
    else:
        print(f'Ordem decrescente: {n3, n2, n1}')