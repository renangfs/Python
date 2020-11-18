print("---------------------------------")
print("-------- EX numero 2 ------------")
print("---------------------------------")
INCRE=0
MEDIA=0
SOMA=0
NUM1 = int(input("Digite um numero:..."))
while NUM1 > 0:
    INCRE = INCRE + 1
    SOMA = SOMA + NUM1
    MEDIA = SOMA / INCRE
    NUM1 = int(input("Digite outro numero para ser calculado a media ou um numero negativo para sair:..."))
print("A soma dos numeros é:{}".format(MEDIA))
