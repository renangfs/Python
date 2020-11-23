print("_____*_____"*6) 
print("Código --- Especificação --- Preço unitário")
print("100 ------ Cachorro quente ------- 5.30")
print("101 ------ Refrigerante ---------- 6.00")
print("102 ------ Hamburguer ------------ 3.20")
print("_____*_____"*6) 
HIS = []
C1 = 1
X1 = 999666999
while X1 != 0:
    print("************ PEDIDO NUMERO:",C1,"****************")
    C1=C1+1
    COD = int ( input ("Digite o codigo do item pedido: ..."))
    QTD = int ( input ("Digite a quantidade do item pedido: ..."))
    if COD==100:
       VALTOT=5.30*QTD
    elif COD==101:
       VALTOT=6.00*QTD
    elif COD==102:
       VALTOT=3.20*QTD
    X1 = int(input("Para continuar digite(1)para sair digite(0): ..."))
    print("O valor a ser pago é:{:.2f}".format(VALTOT))
    HIS.append(VALTOT)
print("*******"*9) 
print("Obs: A Conta[n] com maior numero total deve ser paga")   
print("*******"*9) 
print("Conta [1] R$:{:.2f}".format(HIS[0]))
print("Conta [2] R$:{:.2f}".format(HIS[0]+HIS[1]))
print("Conta [3] R$:{:.2f}".format(HIS[0]+HIS[1]+HIS[2]))
print("Conta [4] R$:{:.2f}".format(HIS[0]+HIS[1]+HIS[2]+HIS[3]))
print("Conta [5] R$:{:.2f}".format(HIS[0]+HIS[1]+HIS[2]+HIS[3]+HIS[4]))
print("Conta [6] R$:{:.2f}".format(HIS[0]+HIS[1]+HIS[2]+HIS[3]+HIS[4]+HIS[5]))
print("Conta [7] R$:{:.2f}".format(HIS[0]+HIS[1]+HIS[2]+HIS[3]+HIS[4]+HIS[5]+HIS[6]))
print("Conta [8] R$:{:.2f}".format(HIS[0]+HIS[1]+HIS[2]+HIS[3]+HIS[4]+HIS[5]+HIS[6]+HIS[7]))
print("Conta [9] R$:{:.2f}".format(HIS[0]+HIS[1]+HIS[2]+HIS[3]+HIS[4]+HIS[5]+HIS[6]+HIS[7]+HIS[8]))
print("Conta [10] R$:{:.2f}".format(HIS[0]+HIS[1]+HIS[2]+HIS[3]+HIS[4]+HIS[5]+HIS[6]+HIS[7]+HIS[8]+HIS[9]))
