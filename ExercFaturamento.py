# exercício 2 - faturamento anual e bonus
valor_faturamento = float(input("Informe o valor do faturamento anual R$ "))
print(''' Informe o nível de seu plano
[1] Basic
[2] Silver
[3] Gold
[4] Platinum ''')

total = 0.0
opcao =  input('Digite a opção ')
if opcao == '1':
    total = (valor_faturamento * 30 / 100)
elif opcao == '2':
    total = (valor_faturamento * 20 / 100)
elif opcao == '3':
    total = (valor_faturamento * 10 / 100)
elif opcao == '4':
    total = (valor_faturamento * 5 / 100)
print('Seu faturamento de R${:.2f} Valor de bônus a ser pago é de R${:.2f}.'.format(valor_faturamento, total))