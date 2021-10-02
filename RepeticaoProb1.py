#Dados uma sequência de 5 num inteiros, calcule a soma de todos os números da sequência
#acumulador
soma = 0
#contador
contador = 0
while contador < 5:
    num = int(input("Informe o num: "))
    soma = soma + num
    contador = contador + 1

print("A soma vale {}".format(soma))


