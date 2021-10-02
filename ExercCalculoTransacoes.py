#Exercício 2 - Cálculo transações
print('{:=^40}'.format('Controle de gastos'))
transacao = int(input("Informe quantas transações financeiras foram realizadas ao longo do dia: "))

soma = 0.0
for i in range(1, transacao + 1 ):
    valor = float(input("Informe o valor da {}ª transação: R$".format(i)))
    soma = soma + valor
print("Você realizou {} transações financeiras, gastando um total de R$ {:.2f}".format(transacao,soma))
print("A média de seus gastos por transação foi de : R$ {:.2f}".format(soma/transacao))
