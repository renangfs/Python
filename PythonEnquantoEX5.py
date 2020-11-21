print ( "---------------------------------------" )
print ( "---------------EX numero5--------------" )
print ( "---------------------------------------" )
print("Código--- Especificação Preço unitário")
print("100 ------ Cachorro quente ------- 1,10")
print("101 ------ Bauru simples ---------- 1,30")
print("102 ------ Bauru c/ovo ------------ 1,50")
print("103 ------ Hamburger ------------- 1,10")
print("104 ------ Cheeseburger ---------- 1,30")
print("105 ------ Refrigerante ------------ 1,00")
X1 = 999666999
while X1 !=0 :
    COD = int ( input ("Digite o codigo do item pedido: ..."))
    QTD = int ( input ("Digite a quantidade do item pedido: ..."))
    if COD==100:
       VALTOT=1.10*QTD
    elif COD==101:
       VALTOT=1.30*QTD
    elif COD==102:
      VALTOT=1.50*QTD
    elif COD==103:
      VALTOT=1.10*QTD
    elif COD==104:
      VALTOT=1.30*QTD
    elif COD==105:
      VALTOT=1.00*QTD
    print("O valor a ser pago é:{:.2f}".format(VALTOT))
    X1 = int(input("Para continuar digite(1)para sair digite(0): ..."))
print("---------------------------------")
print("-------- Fim de Processo --------")
print("---------------------------------")
