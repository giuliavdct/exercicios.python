#exercício 2 - Faturamento Anual

altura = float(input('Qual sua altura? (m) '))
peso = float(input('Qual seu peso? (kg) '))
imc = peso/(altura ** 2)
print('Seu índice de massa corporal é {:.2f}'.format(imc))
if imc < 16.00:
    print('Baixo peso Grau III')
elif 16.00 <= imc < 16.99:
    print('Baixo peso Grau II')
elif 17.00 <= imc < 18.49:
    print('Baixo peso Grau I')
elif 18.50 <= imc < 24.99:
    print('Peso ideal')
elif 25.00 <= imc < 29.99:
    print('Sobrepeso')
elif 30.00 <= imc < 34.99:
    print('Obesidade grau I')
elif 35.00 <= imc < 39.99:
    print('Obesidade grau II')
elif imc < 40.00:
    print('Obesidade grau II')