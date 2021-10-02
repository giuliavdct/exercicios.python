# Desenvolva um algoritmo que informe se uma data é válida ou não. O algoritmo deverá ler 2 números inteiros,
# que representem o dia e o mês e informar se é um dia do mês válido. Desconsidere os casos de ano bissexto, ou seja, fevereiro tem 28 dias.
dia = int(input("Informe o dia : "))
mes = int(input("Informe o mês : "))

if dia < 1 or dia > 31 or mes < 1 or mes > 12:
    print("Data Inválida")
elif mes == 2 and dia > 28:
    print("Data inválida")
elif dia == 31 and mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("Data inválida")
else:
    print("Data inválida")