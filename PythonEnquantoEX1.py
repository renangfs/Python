
print("---------------------------------")
print("-------- EX numero 1 ------------")
print("---------------------------------")
SOMATOTAL=0
NUM1 = int(input("Digite um numero:..."))
while NUM1 > 0:
    SOMATOTAL = NUM1 + SOMATOTAL
    NUM1 = int(input("Digite outro numero para ser somado ou um numero negativo para sair:..."))
print("A soma dos numeros é:",SOMATOTAL)
