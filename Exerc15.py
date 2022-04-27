# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax² + bx + c

a = float(input('Valor de A: '))
b = float(input('Valor de B: '))
c = float(input('Valor de C: '))
d = ((b ** 2)-(4*a*c))
delta = d ** 0.5
if d < 0:
    print("Não possui raízes reais")
elif delta == 0:
    x = -b / (2*a)
    print(f"Possui raiz e o valor é {x}")
else:
    x1 = (-b + delta) / (2 * a)
    x2 = (-b - delta) / (2 * a)
    print(f"x'': {x1}, x': {x2}")