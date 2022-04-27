# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
# e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e
# o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5%
# Após o aumento ser realizado, informe na tela: o salário antes do reajuste; o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario_atual = float(input("Digite o seu salário atual: "))
aumento20 = 0.20
aumento15 = 0.15
aumento10 = 0.10
aumento5 = 0.05
salario_reajuste20 = salario_atual * aumento20
salario_reajuste15 = salario_atual * aumento15
salario_reajuste10 = salario_atual * aumento10
salario_reajuste5 = salario_atual * aumento5

if salario_atual <= 280.00:
    salario_novo = salario_atual + salario_reajuste20
    print(f'Seu salário era R${salario_atual:.2f}, teve um aumento de {int(aumento20*100)}% passando para R${salario_novo:.2f}')
elif salario_atual > 280.00 and salario_atual <= 700.00:
    salario_novo = salario_atual + salario_reajuste15
    print(f'Seu salário era R${salario_atual:.2f}, teve um aumento de {int(aumento15*100)}% passando para R${salario_novo:.2f}')
elif salario_atual > 700.00 and salario_atual <= 1500.00:
    salario_novo = salario_atual + salario_reajuste10
    print(
        f'Seu salário era R${salario_atual:.2f}, teve um aumento de {int(aumento10 * 100)}% passando para R${salario_novo:.2f}')
elif salario_atual > 1500.00:
    salario_novo = salario_atual + salario_reajuste5
    print(f'Seu salário era R${salario_atual:.2f}, teve um aumento de {int(aumento5 * 100)}% passando para R${salario_novo:.2f}')