#Jogo de adivinhação

import random
sorteado = random.ramdint(1, 1000)
chute = int("informe seu chute")
tentativas = 1

while chute != sorteado and tentativas <= 10:
    if sorteado < chute:
        print("Tente um número menor")
    elif sorteado > chute :
        print("Tente um número maior")
    chute = int (input("Informe seu chute: "))
    tentativas = tentativas + 1

if chute == sorteado:
    print ("Paranéns !!! Você acertou !!!")
    print("Você fez {} tentativas". format(tentativas))
else:
    print("Você não acertou, o número era {}".format(sorteado))