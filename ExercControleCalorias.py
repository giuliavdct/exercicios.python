#Exercício 1 - Controle de Calorias
print('{:=^40}'.format('Cálculo Diário de Calorias'))

soma = 0
for i in range(5):
    alimento = (input("Informe o alimento consumido: "))
    numero = float(input("Agora, informe as calorias deste alimento: "))
    soma = soma + numero
print("O valor total de calorias consumidos hoje foi de: {:.3f}".format(soma))