# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-Matutino ou V- Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
# ou "Valor Inválido!", conforme o caso

turno = str(input('\n Selecione o turno que você estuda abaixo. \n '
                  '[M - Matutino, V - Vespertino, N - Noite]: ').upper())

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor inválido.")