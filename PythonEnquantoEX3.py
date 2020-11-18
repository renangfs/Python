
print("---------------------------------")
print("-------- EX numero 3 ------------")
print("---------------------------------")
SOMAMENOS = 0
SOMAMAIS = 0
NUM = 0
NUM = int(input("Digite um numero:..."))
while NUM != 0:
     if NUM > 0 :
       SOMAMAIS = SOMAMAIS + 1
       NUM = int(input("Digite um numero:..."))
     if NUM < 0 :
       SOMAMENOS = SOMAMENOS + 1
       NUM = int(input("Digite um numero:..."))

print("A quantidade de numeros positivos é:{} e os numeros negativos é:{}".format(SOMAMAIS,SOMAMENOS))
