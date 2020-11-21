print ( "---------------------------------------" )
print ( "--------------EX numero6---------------" )
print ( "---------------------------------------" )
print("Código -----Cargo------------Percentual")
print("101 ------ Gerente --------------- 10%")
print("102 ------ Engenheiro ------------ 20%")
print("103 ------ Técnico --------------- 30%")
print ( "______________________________________" )
print ( "***codigos maiores que 104 ou menores\n   que 100 obiteram 40% de almento***" )
print ( "______________________________________" )
X = 999666999
while X != 1:
    COD = int(input("Digite o codigo do item pedido: . . ."))
    SAL = int(input("Digite o salario para receber o almento: . . ."))
    if COD==101:
      POR=SAL*0.10
      VALTOT=SAL+POR
      print("---------------10%------------------")
    elif COD==102:
      POR=SAL*0.20
      VALTOT=SAL+POR
      print("---------------20%------------------")
    elif COD==103:
      POR=SAL*0.30
      VALTOT=SAL+POR
      print("---------------30%------------------")
    elif COD>=100 or COD<=104:
      POR=SAL*0.40
      VALTOT=SAL+POR
      print("---------------40%------------------")
    print("O salario antigo era",SAL)
    print("O Valor do salario com o almento é R$:{:.2f} e a diferença é de R$:{:.2f}.".format (VALTOT,VALTOT-SAL))
    X = int(input("Digite (1) para sair e (0)para continuar"))
print("---------------------------------")
print("-------- Fim de Processo --------")
print("---------------------------------") 
