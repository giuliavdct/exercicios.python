#A convers˜ao de graus Fahrenheit para centígrados ´e obtida pela fórmula C = 5/9 (F − 32). Escreva um algoritmo que calcule e
#escreva uma tabela de graus cent´ıgrados em fun¸c˜ao da temperatura em graus Fahrenheit que variem de 50 a 150 Fahrenheit de 1 em 1
fahr = 50
while fahr <= 150:
    celsius = 5 * (50 - 32) / 9
    print ("{} -> {:.1f}".format(fahr, celsius))
    fahr = fahr + 1