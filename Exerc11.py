# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e
# 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.#
# Desconto do IR:
# Salário Bruto até 900 (inclusive) – isento
# Salário Bruto até 1500 (inclusive) – desconto de 5%
# Salário Bruto até 2500 (inclusive) – desconto de 10%
# Salário Bruto acima de 2500 – desconto de 20% Imprima na tela as informações

hora_valor = float(input("Digite o valor da sua hora: "))
horas_mes = float(input("Digite as horas trabalhadas no mês: "))
salario = hora_valor * horas_mes

if salario <= 900:
    desconto = 0
elif salario <= 1500:
    desconto = salario * 0.05
elif salario <= 2500:
    desconto = salario * 0.10
else:
    desconto = salario * 0.20

sindicato = salario * 0.03
fgts = salario * 0.11
salario_liquido = salario - desconto - sindicato

print(f'\n Salário bruto: R${salario}\n'
      f'\n -------- Descontos ---------- \n'
      f'\n Sindicato: R${sindicato} \n'
      f'\n Imposto de renda: R${desconto}\n'
      f'\n ------------------------------\n'
      f'\n Salário Líquido: R${salario_liquido}\n'
      f'\n ------------------------------\n'
      f'\n FGTS: R${fgts}\n')
