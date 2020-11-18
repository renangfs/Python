
print("---------------------------------")
print("-------- EX numero 3 ------------")
print("---------------------------------")
SOMAMENOS = 0
SOMAMAIS = 0
NUM = 0
NUM = float(input("Digite um numero:..."))
while NUM != 0:
     if NUM > 0 :
       SOMAMAIS = SOMAMAIS + 1
     elif NUM < 0 :
       SOMAMENOS = SOMAMENOS + 1
     else:
        print("A quantidade de numeros positivos é:{} e os numeros negativos é:{}".format(SOMAMAIS,SOMAMENOS)) 
   NUM = float(input("Digite um numero:..."))
