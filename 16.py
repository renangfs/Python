num=float(input("Digite um numero real:"))
print("O numero tansformado para inteiro é:{:.0f}".format(num))

ou

num = float(input("Digiote"))
muda=int(num)
print("O numero é {}".format(muda))


ou 

#funciona so com a biblioteca matematica baixada
import math
num = float(input("Digite o numero: "))
print("O numero digitado foi {} e o numero na parte inteira é {}".format(num,math.trunc(muda)))