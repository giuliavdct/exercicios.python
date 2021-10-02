#Validação de dados, Garanta de que as notas informadas estejam no intervalo entre 0 e 10.
nota = float(input("nota: "))

while nota < 0 or nota > 10:
    print("Nota inválida, digite novamente")
    nota = float(input("nota: "))

print(nota)